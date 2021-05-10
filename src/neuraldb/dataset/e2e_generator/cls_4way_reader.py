from typing import Iterable

import torch
from torch.utils.data import TensorDataset
from transformers import PreTrainedTokenizer

from neuraldb.dataset.answer_type import AnswerType
from neuraldb.dataset.classification_example import (
    ClassificationExample,
    PaddedClassificationFeatures,
)
from neuraldb.dataset.instance_generator import InstanceGenerator
from neuraldb.dataset.search_engines.return_all import ReturnAll
from neuraldb.search_engine import SearchEngine


class Classify4WaySpecificGenerator(InstanceGenerator):
    contextual_answer_special = "[CONTEXT_LOOKUP]"

    def __init__(
        self,
        tokenizer: PreTrainedTokenizer,
        update_search: SearchEngine = ReturnAll(),
        context_limit: int = 256,
    ):
        super().__init__(tokenizer, update_search, context_limit)

        self.labels = [
            self.contextual_answer_special,
            self.yes_answer_special,
            self.no_answer_special,
            self.null_answer_special,
        ]
        self.labels_to_idx = {label: id for id, label in enumerate(self.labels)}

    def _generate_instances(self, context, query, answer, metadata=None):
        encoded = self._tokenizer.encode_plus(
            self.concatenate_context(context), query, is_pretokenized=True
        )
        yield ClassificationExample(
            encoded["input_ids"], encoded["token_type_ids"], self.labels_to_idx[answer]
        )

    def _preprocess_answer(self, answer, answer_type):
        if answer_type == AnswerType.NULL_ANSWER:
            return self.null_answer_special
        elif answer_type == AnswerType.BOOL_ANSWER:
            return (
                self.yes_answer_special if answer == "Yes" else self.no_answer_special
            )
        else:
            return self.contextual_answer_special

    def pad(self, example):
        attention_mask = self.apply_padding([1] * len(example.token_ids))
        token_ids = self.apply_padding(example.token_ids)
        token_type_ids = self.apply_padding(example.token_type_ids)

        assert len(token_ids) == len(token_type_ids)

        return PaddedClassificationFeatures(
            token_ids, token_type_ids, attention_mask, example.label_idx
        )

    def to_tensor_dataset(self, examples: Iterable[PaddedClassificationFeatures]):
        all_examples = list(examples)
        all_token_ids = torch.LongTensor([ex.token_ids for ex in all_examples])
        all_attention_mask = torch.LongTensor(
            [ex.attention_mask for ex in all_examples]
        )
        all_token_type_ids = torch.LongTensor([ex.token_ids for ex in all_examples])
        all_labels = torch.LongTensor([ex.label_idx for ex in all_examples])

        return TensorDataset(
            all_token_ids, all_attention_mask, all_token_type_ids, all_labels
        )
