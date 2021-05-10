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


class Seq2SeqSpecificGenerator(InstanceGenerator):
    def __init__(
        self,
        tokenizer: PreTrainedTokenizer,
        update_search: SearchEngine = ReturnAll(),
        context_limit: int = 256,
        answer_limit: int = 32,
        unlimited_budget: bool = False,
        test_mode: bool = False,
        is_oracle: bool = False,
        iterate: bool = False,
    ):
        super().__init__(
            tokenizer,
            update_search,
            context_limit=context_limit,
            unlimited_budget=unlimited_budget,
            is_oracle=is_oracle,
            iterate=iterate,
        )
        self.answer_limit = answer_limit
        self.list_sep = "[LIST]"
        self.special_labels = {
            self.null_answer_special,
            self.yes_answer_special,
            self.no_answer_special,
            self.empty_list_answer_special,
        }
        self._tokenizer.add_tokens("[QRY]")
        self._tokenizer.add_tokens(self.list_sep)
        self.test_mode = test_mode

    def _generate_instances(self, context, query, answer, metadata=None):
        # print("*" * 80)
        # print(f"Input: {self.concatenate_context(context),['[QRY] '] + query}")
        # print(f"Output: {answer+' '+self._tokenizer.eos_token}")
        # print("*"*80)
        encoded = self._tokenizer.encode_plus(
             query + ["[QRY]"], self.concatenate_context(context), is_pretokenized=True,
        )
        assert len(encoded["input_ids"]) <= self._context_limit

        encoded_answer = self._tokenizer.encode_plus(
            answer + " " + self._tokenizer.eos_token, is_pretokenized=True
        )

        if len(encoded_answer["input_ids"]) > self.answer_limit and not self.test_mode:
            logger.error(
                "Tokenized answer exceeds length limit: \nQuery: {}\nTokenized Answer:{}".format(
                    query,
                    answer,
                )
            )
            return

        assert (
            len(encoded["input_ids"]) <= self._context_limit
        ), "Got string of length {} for limit of {}".format(
            len(encoded["input_ids"]), self._context_limit
        )

        yield GenerationExample(
            encoded["input_ids"],
            encoded_answer["input_ids"],
            self._tokenizer.convert_ids_to_tokens(encoded_answer["input_ids"]),
            metadata,
        )

    def _preprocess_answer(self, answer, answer_type):
        if answer_type == AnswerType.NULL_ANSWER:
            return self.null_answer_special
        elif answer_type == AnswerType.BOOL_ANSWER:
            return (
                self.yes_answer_special if answer == "Yes" or answer == True else self.no_answer_special
            )
        elif answer_type == AnswerType.EMPTY_LIST_ANSWER:
            return self.empty_list_answer_special
        elif answer_type == AnswerType.LIST_ANSWER:
            return " [LIST] ".join(answer)
        else:
            return answer

    def pad(self, example):
        attention_mask = self.apply_padding([1] * len(example.token_ids))
        token_ids = self.apply_padding(example.token_ids)

        if example.label_ids is not None:
            decoder_attention_mask = self.apply_padding(
                [1] * len(example.label_ids), self.answer_limit or self.answer_limit
            )
            decoder_token_ids = self.apply_padding(
                example.label_ids, self.answer_limit or self.answer_limit
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

    def interactive(self, query_tokens, context_tokens):
        encoded = self._tokenizer.encode_plus(
            self.concatenate_context(context_tokens),
            ["[QRY] "] + query_tokens,
            is_pretokenized=True,
        )
        return GenerationExample(encoded["input_ids"], None, None, None)

    def collate_fn(self, batch: Iterable[PaddedGenerationFeatures]):

        input_ids = torch.LongTensor([x.input_ids for x in batch])
        attention_mask = torch.LongTensor([x.attention_mask for x in batch])
        metadata = [i.metadata for i in batch]

        if not self.test_mode:
            decoder_input_ids = torch.LongTensor([x.decoder_input_ids for x in batch])
            lm_labels = torch.LongTensor([x.lm_labels for x in batch])
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
                "decoder_input_ids": [x.decoder_input_ids for x in batch],
                "metadata": metadata,
            }

class V1Seq2SeqSpecificGenerator(Seq2SeqSpecificGenerator):
    def _preprocess_answer(self, answer, answer_type):
        pp = lambda a: self.null_answer_special if a is None else (str(a) if isinstance(a, str) or isinstance(a,int) or isinstance(a,float) else (self.yes_answer_special if a else self.no_answer_special))
        return " [LIST] ".join([pp(a) for a in answer]) if len(answer) else self.null_answer_special
