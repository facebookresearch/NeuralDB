import abc
import itertools
import logging
from typing import List
from transformers import PreTrainedTokenizer, LEDTokenizer

logger = logging.getLogger(__name__)


class InstanceGenerator(abc.ABC):
    empty_context_special = "[EMPTY_CONTEXT]"
    null_answer_special = "[NULL_ANSWER]"
    empty_list_answer_special = "[EMPTY_LIST_ANSWER]"
    yes_answer_special = "[YES_ANSWER]"
    no_answer_special = "[NO_ANSWER]"
    context_delimiter = "[CONTEXT]"
    query_delimiter = "[QUERY]"
    answer_delimiter = "[ANSWER]"
    sep_special = "[SEP]"
    sym_special = "[SYM]"

    def __init__(
        self,
        tokenizer: PreTrainedTokenizer,
        maximum_source_length=256,
        maximum_target_length=64,
        padding=None,
        ignore_pad_token_for_loss=True,
        test_mode=False,
        subsampler=None,
    ) -> object:
        self.test_mode = test_mode
        self.subsampler = subsampler

        logger.info("Generating instances with {} tokenizer".format(repr(tokenizer)))
        self.tokenizer = tokenizer

        logger.info("Adding special token types")
        self.tokenizer.add_tokens(self.empty_context_special, special_tokens=False)
        self.tokenizer.add_tokens(self.context_delimiter, special_tokens=False)
        self.tokenizer.add_tokens(self.query_delimiter, special_tokens=False)
        self.tokenizer.add_tokens(self.answer_delimiter, special_tokens=False)

        self.tokenizer.add_tokens(self.null_answer_special, special_tokens=False)
        self.tokenizer.add_tokens(self.empty_list_answer_special, special_tokens=False)
        self.tokenizer.add_tokens(self.yes_answer_special, special_tokens=False)
        self.tokenizer.add_tokens(self.no_answer_special, special_tokens=False)
        self.tokenizer.add_tokens(self.sep_special, special_tokens=False)
        self.tokenizer.add_tokens(self.sym_special, special_tokens=False)

        self.max_source_length = maximum_source_length
        self.max_target_length = maximum_target_length
        self.padding = padding
        self.ignore_pad_token_for_loss = ignore_pad_token_for_loss

        self.context_delimiter_tokens = [self.context_delimiter]
        self.answer_delimiter_tokens = [self.answer_delimiter]

    def generate(self, database, database_idx=None):
        return self._generate(database, database_idx)

    def concatenate_context(self, context):
        delimited_context = [
            c + (self.context_delimiter_tokens if idx < len(context) - 1 else [])
            for idx, c in enumerate(context)
        ]
        return (
            list(itertools.chain(*delimited_context))
            if len(context)
            else [self.empty_context_special]
        )

    def concatenate_answer(self, answers):
        delimited_answers = [
            c + (self.answer_delimiter_tokens if idx < len(answers) - 1 else [])
            for idx, c in enumerate(answers)
        ]
        return (
            list(itertools.chain(*delimited_answers))
            if len(answers)
            else [self.null_answer_special]
        )

    def maybe_tokenize_answer(self, answer):
        return (
            self.tokenizer.tokenize(str(answer))
            if answer not in {"TRUE", "FALSE"}
            else (
                [self.yes_answer_special]
                if answer == "TRUE"
                else [self.no_answer_special]
            )
            if len(answer)
            else [self.null_answer_special]
        )

    def maybe_tokenize_db(self, db_text):
        return map(self.tokenizer.tokenize, db_text)

    def _generate(self, database, database_idx):
        # Tokenize Updates
        db_text = database["updates"]
        update_tokens = list(self.maybe_tokenize_db(db_text))

        # Process all queries
        for query_idx, query in enumerate(database["queries"]):
            query["database_idx"] = database_idx
            query["question_idx"] = query_idx

            if (
                not self.test_mode
                and self.subsampler is not None
                and self.subsampler.maybe_drop_sample(query)
            ):
                continue

            yield from self._process_query(query, update_tokens)

    @abc.abstractmethod
    def _process_query(self, query, update_tokens):
        raise NotImplementedError("not implemented")

    def apply_padding(self, toks: List[int], limit=None):
        if limit is None:
            limit = self._context_limit

        padding = [0] * (limit - len(toks))
        return toks + padding

    def encode(self, example):
        query_str = self.tokenizer.decode(
            self.tokenizer.convert_tokens_to_ids(example["query"])
        )
        context_strs = [
            self.tokenizer.decode(self.tokenizer.convert_tokens_to_ids(context))
            for context in example["context"]
        ]

        encoded = self.tokenizer.encode_plus(
            query_str, f" {self.context_delimiter} ".join(context_strs)
        )

        if type(self.tokenizer) == LEDTokenizer:
            encoded["global_attention_mask"] = [
                1 if idx <= len(example["query"]) + 1 else 0
                for idx in range(len(encoded["input_ids"]))
            ]
            assert len(encoded["global_attention_mask"]) == len(
                encoded["attention_mask"]
            )
            assert len(encoded["input_ids"]) == len(encoded["attention_mask"])

        if "output" in example:
            output_strs = [
                a.strip()
                for a in self.tokenizer.decode(
                    self.tokenizer.convert_tokens_to_ids(example["output"])
                ).split(self.answer_delimiter)
            ]

            with self.tokenizer.as_target_tokenizer():
                encoded_target = self.tokenizer.encode_plus(
                    f" {self.answer_delimiter} ".join(output_strs)
                )
                encoded["labels"] = encoded_target["input_ids"]

        if "metadata" in example:
            encoded["metadata"] = example["metadata"]

        return encoded

        # query_ids = self.tokenizer.convert_tokens_to_ids(example["query"])
        # context_ids = self.tokenizer.convert_tokens_to_ids(
        #     self.concatenate_context(example["context"])
        # )
        #
        # in_ids = (
        #     query_ids
        #     + self.tokenizer.convert_tokens_to_ids([self.query_delimiter])
        #     + context_ids
        # )
        # in_mask = [1 for _ in in_ids]
        #
        #
        #
        # encoded = {"input_ids": in_ids, "attention_mask": in_mask}
        #
        # if "metadata" in example:
        #     encoded["metadata"] = example["metadata"]
        #
        # if "output" in example:
        #     encoded["labels"] = self.tokenizer.convert_tokens_to_ids(
        #         example["output"]
        #     ) + [self.tokenizer.eos_token_id]
        #
        # return encoded

    def fusion_encode(self, example):
        query_str = self.tokenizer.decode(
            self.tokenizer.convert_tokens_to_ids(example["query"])
        )

        if not len(example["context"]):
            example["context"].append([self.empty_context_special])

        context_strs = [
            self.tokenizer.decode(self.tokenizer.convert_tokens_to_ids(context))
            for context in example["context"]
        ]

        encoded_contexts = [
            self.tokenizer.encode_plus(query_str, context_str)
            for context_str in context_strs
        ]

        encoded = {}
        encoded["context_ids"] = [
            encoded_context["input_ids"] for encoded_context in encoded_contexts
        ]
        encoded["context_mask"] = [
            encoded_context["attention_mask"] for encoded_context in encoded_contexts
        ]

        if "output" in example:
            output_strs = [
                a.strip()
                for a in self.tokenizer.decode(
                    self.tokenizer.convert_tokens_to_ids(example["output"])
                ).split(self.answer_delimiter)
            ]

            with self.tokenizer.as_target_tokenizer():
                encoded_target = self.tokenizer.encode_plus(
                    f" {self.answer_delimiter} ".join(output_strs)
                )
                encoded["labels"] = encoded_target["input_ids"]

        if "metadata" in example:
            encoded["metadata"] = example["metadata"]

        return encoded

    def maybe_decorate_with_metadata(self, instance, query_obj):
        if False and not self.test_mode:
            return instance

        if "metadata" not in instance:
            instance["metadata"] = {}

        instance["metadata"].update(
            {
                "relation": query_obj["relation"],
                "id": query_obj["id"],
                "type": query_obj["type"],
                "question": query_obj["query"],
                "database_idx": query_obj["database_idx"],
                "question_idx": query_obj["question_idx"],
            }
        )

        # A dumb fix because HuggingFace won't run predictions without a decoder output
        if "output" not in instance:
            instance["output"] = [self.tokenizer.eos_token]

        return instance
