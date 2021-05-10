from functools import partial
from typing import Iterable

import logging
import torch

from lightning_base import MODEL_MODES
from neuraldb.dataset.generation_example import (
    GenerationExample,
    PaddedGenerationFeatures,
)
from neuraldb.dataset.e2e_generator.seq2seq_reader import Seq2SeqSpecificGenerator

logger = logging.getLogger(__name__)


class DeferredSeq2SeqSpecificGenerator(Seq2SeqSpecificGenerator):
    def _resolve_context(self, context, query_string, query_tokens):
        self.update_search.set_document_database(context)
        scores = self.update_search.find_top_k(query_string)
        sort_scores = scores.sort(descending=True)

        toks = self._tokenizer.batch_encode_plus(context, add_special_tokens=False)

        if "input_ids" in toks:
            filtered_sents, filtered_indices = self.aa_filter_context(
                toks["input_ids"],
                self._context_limit - len(query_tokens) - 1 - 2,
                sort_scores[1],
            )
            concat_context = self.concatenate_context(filtered_sents)

            if len(filtered_sents) > 0:
                # for tokens, page_index in zip(filtered_sents, filtered_indices):
                # if scores[page_index].grad is not None:
                #    scores[page_index].grad/=len(tokens)

                scale = torch.cat(
                    [
                        scores[page_index].expand(len(tokens))
                        for tokens, page_index in zip(filtered_sents, filtered_indices)
                    ]
                )
                assert not (
                    self.update_search._encoder.training and scale.grad_fn is None
                )
                assert len(scale) == len(concat_context)
                pad_scale = torch.cat(
                    [
                        scale,
                        torch.FloatTensor(
                            (self._context_limit - len(concat_context)) * [1.0]
                        ),
                    ]
                )
                assert len(pad_scale) == self._context_limit

                return (
                    self._tokenizer.encode_plus(
                        concat_context, ["[QRY] "] + query_tokens, is_pretokenized=True
                    ),
                    pad_scale,
                    {
                        "scores": [scores[idx] for idx in filtered_indices],
                        "context_texts": list(
                            map(self._tokenizer.decode, filtered_sents)
                        ),
                    },
                )

        return (
            self._tokenizer.encode_plus(
                ["[QRY] "] + query_tokens, is_pretokenized=True
            ),
            torch.FloatTensor(self._context_limit * [1.0]),
            {"scores": [], "context_texts": []},
        )

    def _promise_encoded_context(self, context, query_string, query_tokens):
        return partial(self._resolve_context, context, query_string, query_tokens)

    def _generate_instances(self, context, query, answer, metadata):
        encoded_promise = self._promise_encoded_context(
            context, self._tokenizer.convert_tokens_to_string(query), query
        )
        encoded_answer = self._tokenizer.encode_plus(
            answer + " " + self._tokenizer.eos_token, is_pretokenized=True
        )

        if metadata is None:
            metadata = {}
        metadata["query_text"] = self._tokenizer.convert_tokens_to_string(query)

        if len(encoded_answer["input_ids"]) > self.answer_limit:
            logger.error(
                "Tokenized answer exceeds length limit: \nQuery: {}\nTokenized Answer:{}".format(
                    query,
                    answer,
                )
            )

        yield GenerationExample(
            encoded_promise,
            encoded_answer["input_ids"],
            self._tokenizer.convert_ids_to_tokens(encoded_answer["input_ids"]),
            metadata,
        )

    def collate_fn(self, batch: Iterable[GenerationExample]):
        encoded = [x.token_ids() for x in batch]
        # retriever_bias = torch.FloatTensor([self.apply_padding(x[2], self._context_limit) for x in encoded])
        input_ids = torch.LongTensor(
            [
                self.apply_padding(x[0]["input_ids"], self._context_limit)
                for x in encoded
            ]
        )
        attention_mask = torch.LongTensor(
            [
                self.apply_padding(x[0]["attention_mask"], self._context_limit)
                for x in encoded
            ]
        )
        decoder_input_ids = torch.LongTensor(
            [self.apply_padding(x.label_ids, self.answer_limit) for x in batch]
        )
        lm_labels = torch.LongTensor(
            [
                self.apply_padding([1] * len(x.label_ids), self.answer_limit)
                for x in batch
            ]
        )

        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "decoder_input_ids": decoder_input_ids,
            "lm_labels": lm_labels,
            "scale": torch.stack([x[1] for x in encoded]),
            "debug_input_query": [x.metadata["query_text"] for x in batch],
            "debug_input_evidence": [
                [
                    (a.cpu().item(), b)
                    for a, b in zip(x[2]["scores"], x[2]["context_texts"])
                ]
                for x in encoded
            ],
        }

    # Filtering in this reader is deferred so for now, just include what's in the context
    def filter_context(self, updates, context_height, budget, search_results=None):
        return [updates[:context_height]]

    def aa_filter_context(self, updates, budget, search_results=None):

        # If we returned no results, then return an empty list and don't bother trying to iterate over the search results
        if (
            search_results is None
            or search_results.size() == 0
            or search_results.dim() == 0
            or not len(search_results)
        ):
            return [], []

        filtered = []
        collected = []
        for sentence_index in search_results:
            tokens = updates[sentence_index]
            if (
                len(tokens)
                + sum(len(a) for a in filtered)
                + len(self._delimiter_tokens) * len(filtered)
                > budget
            ):
                break
            else:
                filtered.append(tokens)
                collected.append(sentence_index)

        return filtered, collected

    # We don't need tokenize the inputs for the DB when reading the original data (we could do this later)
    def maybe_tokenize_db(self, db_text):
        return db_text
