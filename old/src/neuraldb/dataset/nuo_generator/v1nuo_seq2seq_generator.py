from functools import reduce
import random
from typing import Iterable

import logging
import torch
from transformers import PreTrainedTokenizer
from neuraldb.dataset.e2e_reader.v1_0_database_reader import V10DatabaseSpecificReader
from neuraldb.dataset.generation_example import (
    GenerationExample,
    PaddedGenerationFeatures,
)
from neuraldb.dataset.instance_generator import InstanceGenerator


logger = logging.getLogger(__name__)


class V1NUOSeq2SeqSpecificGenerator(InstanceGenerator):
    def __init__(
        self,
        tokenizer: PreTrainedTokenizer,
        context_limit: int = 256,
        answer_limit: int = 32,
        filter_types: Iterable[str] = None,
        unlimited_budget: bool = False,
        test_mode: bool = False,
        generate_random: bool = False
    ):
        super().__init__(
            tokenizer,
            None,
            context_limit=context_limit,
            unlimited_budget=unlimited_budget,
        )
        self.generate_random = generate_random
        self.use_test = False

        self.filter_types = filter_types
        self.answer_limit = answer_limit
        self.special_labels = {
            self.null_answer_special,
            self.yes_answer_special,
            self.no_answer_special,
            self.empty_list_answer_special,
        }

        self._tokenizer.add_tokens("[QRY]")
        self._tokenizer.add_tokens("[SET]")
        self._tokenizer.add_tokens("[COUNT]")
        self._tokenizer.add_tokens("[BOOL]")
        self._tokenizer.add_tokens("[ARG]")
        self._tokenizer.add_tokens("[MMX]")
        self._tokenizer.add_tokens("[SEP]")
        self._tokenizer.add_tokens("[SYM]")
        self._tokenizer.add_tokens("[EMPTY]")
        self.v1_reader = V10DatabaseSpecificReader()
        self.test_mode = test_mode

    def interactive(self, query, fact):
        query_tokens = self._tokenizer.tokenize(query)
        fact_tokens = self._tokenizer.tokenize(fact)
        encoded = self._tokenizer.encode_plus(
            fact_tokens, ["[QRY]"] + query_tokens, is_pretokenized=True
        )
        return GenerationExample(encoded["input_ids"], None, None, None)

    def _generate(self, instances):
        for idx, instance in enumerate(instances):
            if self.filter_types is not None and instance["prop"] in self.filter_types:
                continue

            fact_tokens = [self._tokenizer.tokenize(fact) for fact in instance["facts"]]

            for qidx, query in enumerate(instance["queries"]):
                query["db_id"] = idx
                query["query_id"] = qidx

                query_tokens = self._tokenizer.tokenize(query["question"] if "question" in query else query["query"])

                if self.generate_random and not self.test_mode:

                    for fact in query["facts"]:
                        if random.uniform(0, 1) < .6:
                            flat_facts = []

                            for f in query["facts"]:
                                if isinstance(f,list):
                                    flat_facts.extend(f)
                                else:
                                    flat_facts.append(f)

                            population = list(set(range(len(instance['facts']))).difference(flat_facts))
                            if len(population):
                                negative = random.sample(population, k=min(len(population),random.randint(1, 3)))
                                projection_tokens = self._tokenizer.tokenize(self.null_answer_special)
                                context = reduce(lambda a, b: a + ["[SEP]"] + b, [fact_tokens[i] for i in negative])

                                yield from filter(
                                    lambda inst: inst is not None,
                                    self._generate_instances(
                                        query_tokens, context, projection_tokens, query
                                    ),
                                )



                if "predicted_facts" in query:
                    self.use_test = True
                    for fact, derv in zip(query["facts"], query["derivations"]):
                        if isinstance(fact, list):
                            context = reduce(lambda a, b: a + ["[SEP]"] + b, [fact_tokens[i] for i in fact])
                        else:
                            context = fact_tokens[fact]


                        yield from filter(
                            lambda inst: inst is not None,
                            self._generate_test_instances(
                                query_tokens, context, query
                            ),
                        )
                else:
                    assert self.use_test == False
                    for fact, derv in zip(query["facts"], query["derivations"]):
                        projection_preprocessed = self._preprocess_answer(
                            derv, query["type"]
                        )

                        if isinstance(fact,list):
                            context = reduce(lambda a,b: a+["[SEP]"]+b, [fact_tokens[i] for i in fact])
                        else:
                            context = fact_tokens[fact]

                        projection_tokens = self._tokenizer.tokenize(projection_preprocessed)
                        yield from filter(
                            lambda inst: inst is not None,
                            self._generate_instances(
                                query_tokens, context, projection_tokens, query
                            ),
                        )



    def _generate_instances(self, query, fact, answer, metadata=None):
        encoded = self._tokenizer.encode_plus(
            fact, ["[QRY]"] + query, is_pretokenized=True
        )
        encoded_answer = self._tokenizer.encode_plus(
            answer + [self._tokenizer.eos_token], is_pretokenized=True
        )

        if len(encoded["input_ids"]) >= self._context_limit:
            return

        assert (
            len(encoded["input_ids"]) <= self._context_limit
        ), "Got string of length {} for limit of {}\nString: {}".format(
            len(encoded["input_ids"]), self._context_limit, fact
        )
        yield GenerationExample(
            encoded["input_ids"],
            encoded_answer["input_ids"],
            self._tokenizer.convert_ids_to_tokens(encoded_answer["input_ids"]),
            metadata,
        )


    def _generate_test_instances(self, query, fact, metadata=None):
        encoded = self._tokenizer.encode_plus(
            fact, ["[QRY]"] + query, is_pretokenized=True
        )

        if len(encoded["input_ids"]) >= self._context_limit:
            return

        assert (
            len(encoded["input_ids"]) <= self._context_limit
        ), "Got string of length {} for limit of {}\nString: {}".format(
            len(encoded["input_ids"]), self._context_limit, fact
        )
        yield GenerationExample(
            encoded["input_ids"],
            None,
            None,
            metadata,
        )


    def _preprocess_answer(self, answer, answer_type):
        if answer is None:
            return self.null_answer_special
        elif answer_type == "set":
            return "[SET] " + answer
        elif answer_type == "count":
            return "[COUNT] " + answer
        elif answer_type == "argmin" or answer_type == "argmax":
            return "[ARG] " + answer
        elif answer_type == "min" or answer_type == "max":
            return "[MMX] " + answer
        else:
            return "[BOOL] " + answer

    def pad(self, example, max_source=None, max_target=None):
        attention_mask = self.apply_padding(
            [1] * len(example.token_ids), max_source or self._context_limit
        )
        token_ids = self.apply_padding(
            example.token_ids, max_source or self._context_limit
        )
        assert len(token_ids) == len(attention_mask)

        if example.label_ids is not None:
            decoder_attention_mask = self.apply_padding(
                [1] * len(example.label_ids), max_target or self.answer_limit
            )
            decoder_token_ids = self.apply_padding(
                example.label_ids, max_target or self.answer_limit
            )
            assert len(decoder_token_ids) == len(decoder_attention_mask)
        else:
            decoder_attention_mask = None
            decoder_token_ids = None

        return PaddedGenerationFeatures(
            token_ids,
            attention_mask,
            decoder_token_ids,
            decoder_attention_mask,
            example.metadata,
        )

    def collate_fn_no_pad(self, padded_batch: Iterable[PaddedGenerationFeatures]):

        input_ids = torch.LongTensor([x.input_ids for x in padded_batch])
        attention_mask = torch.LongTensor([x.attention_mask for x in padded_batch])
        metadata = [i.metadata for i in padded_batch]

        if not self.test_mode:
            decoder_input_ids = torch.LongTensor(
                [x.decoder_input_ids for x in padded_batch]
            )
            lm_labels = torch.LongTensor([x.lm_labels for x in padded_batch])
            return {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "decoder_input_ids": decoder_input_ids,
                "lm_labels": lm_labels,
                "metadata": metadata,
            }
        else:
            return {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "decoder_input_ids": [x.decoder_input_ids for x in padded_batch],
                "metadata": metadata,
            }

    def collate_fn(self, batch: Iterable[GenerationExample]):
        max_source = max(len(x.token_ids) for x in batch)
        max_target = max(
            [len(x.label_ids) for x in batch if x.label_ids is not None] + [0]
        )

        padded_batch = list(map(lambda x: self.pad(x, max_source, max_target), batch))

        input_ids = torch.LongTensor([x.input_ids for x in padded_batch])
        attention_mask = torch.LongTensor([x.attention_mask for x in padded_batch])
        metadata = [i.metadata for i in padded_batch]

        if not self.test_mode:
            decoder_input_ids = torch.LongTensor(
                [x.decoder_input_ids for x in padded_batch]
            )
            lm_labels = torch.LongTensor([x.lm_labels for x in padded_batch])
            return {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "decoder_input_ids": decoder_input_ids,
                "lm_labels": lm_labels,
                "metadata": metadata,
            }
        else:
            return {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "decoder_input_ids": [x.decoder_input_ids for x in padded_batch],
                "metadata": metadata,
            }
