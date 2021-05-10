from typing import Iterable

import logging
import torch
from torch.utils.data import TensorDataset
from transformers import PreTrainedTokenizer

from neuraldb.dataset.answer_type import AnswerType
from neuraldb.dataset.classification_example import PaddedClassificationFeatures
from neuraldb.dataset.generation_example import (
    GenerationExample,
    PaddedGenerationFeatures,
)
from neuraldb.dataset.instance_generator import InstanceGenerator
from neuraldb.dataset.search_engines.return_all import ReturnAll
from neuraldb.search_engine import SearchEngine

logger = logging.getLogger(__name__)


class NUOSeq2SeqSpecificGenerator(InstanceGenerator):
    def __init__(
        self,
        tokenizer: PreTrainedTokenizer,
        context_limit: int = 256,
        answer_limit: int = 32,
        filter_types: Iterable[str] = None,
        unlimited_budget: bool = False,
        test_mode: bool = False,
    ):
        super().__init__(
            tokenizer,
            None,
            context_limit=context_limit,
            unlimited_budget=unlimited_budget,
        )

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
        self._tokenizer.add_tokens("[EMPTY]")

        self.test_mode = test_mode

    def interactive(self, query, fact):
        query_tokens = self._tokenizer.tokenize(query)
        fact_tokens = self._tokenizer.tokenize(fact)
        encoded = self._tokenizer.encode_plus(
            fact_tokens, ["[QRY] "] + query_tokens, is_pretokenized=True
        )
        return GenerationExample(encoded["input_ids"], None, None, None)

    def _generate(self, instances):
        for idx, instance in enumerate(instances):
            if self.filter_types is not None and instance["prop"] in self.filter_types:
                continue

            query_tokens = self._tokenizer.tokenize(instance["query"])
            fact_tokens = self._tokenizer.tokenize(
                " [SEP] ".join([fact for fact in instance["fact"]])
                if len(instance["fact"])
                else "[EMPTY]"
            )
            projection_preprocessed = self._preprocess_answer(
                instance["projection"], instance["type"]
            )
            projection_tokens = self._tokenizer.tokenize(projection_preprocessed)

            yield from filter(
                lambda inst: inst is not None,
                self._generate_instances(
                    query_tokens, fact_tokens, projection_tokens, instance
                ),
            )

    def _generate_instances(self, query, fact, answer, metadata=None):
        encoded = self._tokenizer.encode_plus(
            fact, ["[QRY] "] + query, is_pretokenized=True
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
