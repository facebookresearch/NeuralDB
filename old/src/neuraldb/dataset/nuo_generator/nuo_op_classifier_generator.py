from typing import Iterable

import logging

import os
import torch
from torch.utils.data import TensorDataset
from transformers import PreTrainedTokenizer

from neuraldb.dataset.answer_type import AnswerType
from neuraldb.dataset.classification_example import (
    PaddedClassificationFeatures,
    ClassificationExample,
)
from neuraldb.dataset.generation_example import (
    GenerationExample,
    PaddedGenerationFeatures,
)
from neuraldb.dataset.instance_generator import InstanceGenerator
from neuraldb.dataset.new_classification_example import NewClassificationExample
from neuraldb.dataset.search_engines.return_all import ReturnAll
from neuraldb.search_engine import SearchEngine

logger = logging.getLogger(__name__)


class NUOClassifierGenerator(InstanceGenerator):
    def __init__(
        self,
        tokenizer: PreTrainedTokenizer,
        context_limit: int = 256,
        unlimited_budget: bool = False,
        test_mode: bool = False,
    ):
        super().__init__(
            tokenizer,
            None,
            context_limit=context_limit,
            unlimited_budget=unlimited_budget,
        )
        self.test_mode = test_mode

        self.labels = [
            "lookup",
            "set",
            "count",
            "count_argmin",
            "count_argmax",
            "argmin",
            "argmax",
        ]
        self.labels_to_idx = {v: idx for idx, v in enumerate(self.labels)}

    def _generate(self, instances):
        queries = set()
        for idx, instance in enumerate(instances):
            if "negative" in instance["type"]:
                continue

            if instance["query"] in queries:
                continue

            queries.add(instance["query"])
            query_tokens = self._tokenizer.tokenize(instance["query"])
            yield from self._generate_instances(
                query_tokens, self.labels_to_idx[instance["type"]], instance
            )

            if os.getenv("DEBUG", None) is not None:
                if idx > 1000:
                    break

    def interactive(self, query):
        query_tokens = self._tokenizer.tokenize(query)
        encoded = self._tokenizer.encode_plus(query_tokens, is_pretokenized=True)
        return ClassificationExample(
            encoded["input_ids"], encoded["token_type_ids"], None, None
        )

    def _generate_instances(self, query, label, metadata=None):
        encoded = self._tokenizer.encode_plus(query, is_pretokenized=True)
        assert (
            len(encoded["input_ids"]) <= self._context_limit
        ), "Got string of length {} for limit of {}".format(
            len(encoded["input_ids"]), self._context_limit
        )
        yield ClassificationExample(
            encoded["input_ids"], encoded["token_type_ids"], label, metadata
        )

    def pad(self, example, max_source=None):
        attention_mask = self.apply_padding(
            [1] * len(example.token_ids), max_source or self._context_limit
        )
        token_ids = self.apply_padding(
            example.token_ids, max_source or self._context_limit
        )
        token_type_ids = self.apply_padding(
            example.token_type_ids, max_source or self._context_limit
        )

        assert len(token_ids) == len(attention_mask)
        return PaddedClassificationFeatures(
            token_ids,
            token_type_ids,
            attention_mask,
            example.label_idx,
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
        padded_batch = list(map(lambda x: self.pad(x, max_source), batch))

        input_ids = torch.LongTensor([x.input_ids for x in padded_batch])
        attention_mask = torch.LongTensor([x.attention_mask for x in padded_batch])
        metadata = [i.metadata for i in padded_batch]

        if not self.test_mode:
            labels = torch.LongTensor([x.label for x in padded_batch])
            return {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "labels": labels,
                "metadata": metadata,
            }
        else:
            return {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "metadata": metadata,
            }
