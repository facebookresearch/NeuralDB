import random
from collections import defaultdict
from operator import itemgetter
from typing import Iterable

import logging
import torch
from torch.utils.data import TensorDataset
from tqdm import tqdm
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


class Seq2SeqSpecificSurrogateGenerator(InstanceGenerator):
    def __init__(self, surrogate, downstream_tokenizer, forward):
        self.surrogate_model = surrogate
        self.downstream_reader = downstream_tokenizer
        self._tokenizer = downstream_tokenizer
        self._fwd = forward

    def _generate(self, database):
        db_text = list(map(itemgetter("text"), database["updates"]))
        update_tokens = list(self.maybe_tokenize_db(db_text))
        surrogate_tokens = list(
            self.surrogate_model.data_generator.maybe_tokenize_db(db_text)
        )

        qs = list(database["queries"])
        random.shuffle(qs)
        for query in qs:
            query_tokens = self._tokenizer.tokenize(query["input"])
            context_height = query["context_height"]

            surrogate_query_tokens = (
                self.surrogate_model.data_generator._tokenizer.tokenize(query["input"])
            )
            surrogate_answer_tokens = (
                self.surrogate_model.data_generator._preprocess_answer(
                    query["output"], query["output_type"]
                )
            )

            if (
                surrogate_answer_tokens != self.null_answer_special
                and query["output_type"] != AnswerType.LIST_ANSWER
            ):
                yield list(
                    self._generate_instances(
                        surrogate_tokens[:context_height],
                        surrogate_query_tokens,
                        surrogate_answer_tokens,
                        update_tokens[:context_height],
                        query_tokens,
                    )
                )

    def try_sampling_old(
        self,
        original_prediction,
        surrogate_context,
        surrogate_query,
        removed,
        limit=500,
    ):
        if len(surrogate_context) == 0:  # or limit <= 0:
            # print("Limit expired")
            return []
        samples = [
            s
            for s in random.sample(
                range(len(surrogate_context)), k=len(surrogate_context)
            )
            if s not in removed
        ]

        new_surrogate_instances = []
        for s in samples:
            new_s_context = [
                v for idx, v in enumerate(surrogate_context) if idx not in removed + [s]
            ]
            new_surrogate_instances.append(
                self.surrogate_model.data_generator.interactive(
                    surrogate_query, new_s_context
                )
            )

        results = self._fwd(new_surrogate_instances)

        for idx, result in zip(samples, results):
            yield [removed, idx, result]
            if result == original_prediction:
                yield from self.try_sampling(
                    original_prediction,
                    surrogate_context,
                    surrogate_query,
                    removed + [idx],
                    limit - len(new_surrogate_instances),
                )

    def try_sampling(
        self, original_prediction, surrogate_context, surrogate_query, removed
    ):
        if len(removed) >= len(surrogate_context) - 1:
            return []

        vacant = [a for a in range(len(surrogate_context)) if a not in removed]
        order = random.sample(vacant, k=len(vacant))

        new_surrogate_instances = []
        samples = []
        for i in range(1, len(order)):
            ids = removed + order[:i]
            samples.append(order[:i])
            new_s_context = [
                v for idx, v in enumerate(surrogate_context) if idx not in ids
            ]
            new_surrogate_instances.append(
                self.surrogate_model.data_generator.interactive(
                    surrogate_query, new_s_context
                )
            )

        if len(new_surrogate_instances):
            results = self._fwd(new_surrogate_instances)
        else:
            return []

        for idx, result in zip(samples, results):

            yield [removed + idx[:-1], idx[-1], result]
            # print(removed, idx[:-1], idx[-1], len(order[order.index(idx[-1])+1:]),result)
            if self.does_changes_prediction(original_prediction, result):

                if (
                    len(removed + idx[:-1]) != len(removed)
                    and len(order[order.index(idx[-1]) + 1 :]) > 4
                ):
                    yield from self.try_sampling(
                        original_prediction,
                        surrogate_context,
                        surrogate_query,
                        removed + idx[:-1],
                    )
                else:
                    yield from self.try_sampling(
                        original_prediction,
                        surrogate_context,
                        surrogate_query,
                        (removed + idx)[:-5],
                    )

        # if len(removed):
        #    yield from self.try_sampling(original_prediction, surrogate_context, surrogate_query, removed[:-1])

    def does_changes_prediction(self, original, test):
        if "[LIST]" in original:
            original_split = original.split("[LIST]")
            test_split = test.split("[LSIT]")

            return len(original_split) != len(test_split)
        else:
            return original != test

    def _generate_instances(
        self,
        surrogate_context,
        surrogate_query,
        surrogate_answer,
        master_context,
        master_query,
    ):
        original_prediction = self._fwd(
            [
                self.surrogate_model.data_generator.interactive(
                    surrogate_query, surrogate_context
                )
            ]
        )

        positive_samples = []
        negative_samples = []

        use_count = defaultdict(lambda: defaultdict(int))
        for iters, (removed, idx, prediction) in enumerate(
            self.try_sampling(
                original_prediction[0], surrogate_context, surrogate_query, []
            )
        ):
            if self.does_changes_prediction(original_prediction[0], prediction):
                for a in removed:
                    use_count[idx][a] += 1

                positive_samples.append((removed, idx))

            else:
                negative_samples.append((removed, idx))

            if len(positive_samples) > 20 or iters > 100:
                break

        best_positive = {k: sum(v.values()) for k, v in use_count.items()}
        sorted_best = sorted(best_positive.items(), key=lambda a: a[1], reverse=True)

        budget = 10

        final_positive = []
        for k, count in sorted_best:
            potential_samples = list(
                filter(lambda removed_idx: removed_idx[1] == k, positive_samples)
            )

            for removed, idx in random.sample(
                potential_samples, k=min(len(potential_samples), budget)
            ):
                positive_samples.remove((removed, idx))
                final_positive.append((removed, k))

                if len(final_positive) > budget:
                    break

        final_negative = []
        # if len(positive_samples):
        #    final_negative.extend(random.sample(positive_samples, min(len(positive_samples),max(1,len(final_positive)//2))))
        final_negative.extend(
            random.sample(
                negative_samples,
                min(len(negative_samples), len(final_positive) - len(final_negative)),
            )
        )

        instances = []
        for i in final_positive:
            instances.append((i[0], i[1], 1))
        for i in final_negative:
            instances.append((i[0], i[1], 0))

        random.shuffle(instances)
        for removed_context, idx, label in instances:
            yield self.encode(master_query, master_context, removed_context, idx, label)

    def collate_fn(self, instances):
        longest = max(len(i["input_ids"]) for i in instances)

        return [
            torch.stack(
                [
                    torch.LongTensor(self.apply_padding(x["input_ids"], longest))
                    for x in instances
                ]
            ),
            torch.stack(
                [
                    torch.LongTensor(self.apply_padding(x["attention_mask"], longest))
                    for x in instances
                ]
            ),
            torch.stack([torch.LongTensor([x["label"]]) for x in instances]).squeeze(),
        ]

    def encode(self, master_query, master_context, removed_context, idx, label):
        tokens = []
        tokens.append(self._tokenizer.cls_token)
        tokens.extend(master_query)
        tokens.append(self._tokenizer.sep_token)
        tokens.extend(master_context[idx])
        tokens.append(self._tokenizer.sep_token)
        tokens.append(self._tokenizer.sep_token)

        rset = set(removed_context)
        for c in range(len(master_context)):
            if c not in rset and c != idx:
                if len(tokens) + len(master_context[c]) + 1 > 512:
                    break

                tokens.extend(master_context[c])
                tokens.append(self._tokenizer.sep_token)

        encoded = self._tokenizer.encode_plus(tokens, add_special_tokens=False)
        return {
            "input_ids": encoded["input_ids"],
            "attention_mask": encoded["attention_mask"],
            "label": label,
        }
