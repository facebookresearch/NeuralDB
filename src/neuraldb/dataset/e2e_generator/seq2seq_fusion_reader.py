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
from neuraldb.dataset.multi_generation_example import (
    MultiGenerationExample,
    PaddedMultiGenerationFeatures,
)
from neuraldb.dataset.e2e_generator.seq2seq_reader import Seq2SeqSpecificGenerator
from neuraldb.dataset.search_engines.return_all import ReturnAll
from neuraldb.search_engine import SearchEngine

logger = logging.getLogger(__name__)


class Seq2SeqFusionSpecificGenerator(Seq2SeqSpecificGenerator):
    def _generate_instances(self, context, query, answer, metadata=None):
        encoded_contexts = []

        if len(context) == 0:
            encoded_contexts.append(
                self._tokenizer.encode_plus(
                    [self.empty_context_special],
                    ["[QRY] "] + query,
                    is_pretokenized=True,
                )["input_ids"]
            )
        else:
            # encoded_contexts.append(self._tokenizer.encode_plus(self.concatenate_context(context), ["[QRY] "] + query,
            #                                      is_pretokenized=True)["input_ids"])
            for sentence in context:
                encoded_contexts.append(
                    self._tokenizer.encode_plus(
                        sentence[: self._context_limit - (len(query) + 2)],
                        ["[QRY]"] + query,
                        is_pretokenized=True,
                    )["input_ids"]
                )

        encoded_answer = self._tokenizer.encode_plus(
            answer + " " + self._tokenizer.eos_token, is_pretokenized=True
        )
        assert len(encoded_contexts)

        if len(encoded_answer["input_ids"]) <= self.answer_limit:
            assert (
                len(encoded_answer["input_ids"]) <= self.answer_limit
            ), "Answer was too long: {}\n\n{}\n{}".format(answer, query, metadata)
            yield MultiGenerationExample(
                self._tokenizer.encode_plus(query, is_pretokenized=True)["input_ids"],
                encoded_contexts,
                encoded_answer["input_ids"],
                self._tokenizer.convert_ids_to_tokens(encoded_answer["input_ids"]),
                metadata,
            )

    def pad(self, example):

        context_tokens = []
        context_mask = []
        for token_ids in example.context_ids:
            padded_token_ids = self.apply_padding(token_ids)
            padded_attention_mask = self.apply_padding([1] * len(token_ids))
            assert len(padded_token_ids) == len(padded_attention_mask)
            context_tokens.append(padded_token_ids)
            context_mask.append(padded_attention_mask)

        token_ids = self.apply_padding(example.token_ids)
        attention_mask = self.apply_padding([1] * len(token_ids))

        decoder_token_ids = self.apply_padding(example.label_ids, self.answer_limit)
        decoder_attention_mask = self.apply_padding(
            [1] * len(example.label_ids), self.answer_limit
        )

        assert len(decoder_token_ids) == len(decoder_attention_mask)
        assert len(context_tokens) == len(context_mask)
        assert len(token_ids) == len(attention_mask)
        assert len(context_tokens) and len(context_mask)
        return PaddedMultiGenerationFeatures(
            token_ids,
            attention_mask,
            context_tokens,
            context_mask,
            decoder_token_ids,
            decoder_attention_mask,
            example.metadata,
        )

    def collate_fn(self, batch: Iterable[PaddedGenerationFeatures]):
        input_ids = torch.LongTensor([x.input_ids for x in batch])
        attention_mask = torch.LongTensor([x.attention_mask for x in batch])

        context_ids = [torch.LongTensor(x.context_ids) for x in batch]
        context_mask = [torch.LongTensor(x.context_mask) for x in batch]

        metadata = [i.metadata for i in batch]

        if not self.test_mode:

            decoder_input_ids = torch.LongTensor([x.decoder_input_ids for x in batch])
            lm_labels = torch.LongTensor([x.lm_labels for x in batch])
            return {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "context_ids": context_ids,
                "context_mask": context_mask,
                "decoder_input_ids": decoder_input_ids,
                "lm_labels": lm_labels,
                "metadata": metadata,
            }
        else:
            return {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "context_ids": context_ids,
                "context_mask": context_mask,
                "decoder_input_ids": [x.decoder_input_ids for x in batch],
                "metadata": metadata,
            }

class Seq2SeqV1FusionSpecificGenerator(Seq2SeqFusionSpecificGenerator):
    def _preprocess_answer(self, answer, answer_type):
        pp = lambda a: self.null_answer_special if a is None else (str(a) if isinstance(a, str) or isinstance(a,int) or isinstance(a,float) else (self.yes_answer_special if a else self.no_answer_special))
        return " [LIST] ".join([pp(a) for a in answer]) if len(answer) else self.null_answer_special
