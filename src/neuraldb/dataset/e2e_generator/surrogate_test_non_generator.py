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
from neuraldb.dataset.e2e_reader.v1_0_database_reader import new_guess_answer_type
from neuraldb.dataset.generation_example import (
    GenerationExample,
    PaddedGenerationFeatures,
)
from neuraldb.dataset.instance_generator import InstanceGenerator
from neuraldb.scoring.r_precision import precision, recall
from neuraldb.dataset.search_engines.return_all import ReturnAll
from neuraldb.search_engine import SearchEngine

logger = logging.getLogger(__name__)


class Seq2SeqSpecificSurrogateReader(InstanceGenerator):
    def __init__(self, surrogate, forward):
        self.surrogate_model = surrogate

        self._fwd = forward

    def _generate(self, database):
        db_text = database["facts"]# list(map(itemgetter("text"), database["updates"]))
        surrogate_tokens = list(
            self.surrogate_model.data_generator.maybe_tokenize_db(db_text)
        )

        qs = list(database["queries"])
        # random.shuffle(qs)

        precisions = defaultdict(list)
        recalls = defaultdict(list)
        for query in tqdm(qs):

            context_height = query["height"]

            surrogate_query_tokens = (
                self.surrogate_model.data_generator._tokenizer.tokenize(query["question"])
            )
            surrogate_answer_tokens = (
                self.surrogate_model.data_generator._preprocess_answer(
                    query["answer"], new_guess_answer_type(query["answer"])
                )
            )

            if surrogate_answer_tokens != self.null_answer_special:
                (
                    query["guessed_evidence"],
                    query["positive_samples"],
                    query["negative_samples"],
                ) = self._generate_instances(
                    surrogate_tokens[:context_height],
                    surrogate_query_tokens,
                    surrogate_answer_tokens,
                )

                guessed = [i[0] for i in query["guessed_evidence"]]
                precisions[query["type"]].append(
                    precision(query["facts"], guessed)
                )
                recalls[query["type"]].append(
                    recall(query["facts"], guessed)
                )

                print(
                    [query["type"]],
                    sum(precisions[query["type"]])
                    / len(precisions[query["type"]]),
                    sum(recalls[query["type"]])
                    / len(recalls[query["type"]]),
                )
            else:
                query["guessed_evidence"] = []
                query["positive_samples"] = []
                query["negative_samples"] = []

            yield query

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

        original_list = "[LIST]" in original_prediction
        op = original_prediction
        for idx, result in zip(samples, results):

            yield [removed + idx[:-1], idx[-1], result]
            # print(removed, idx[:-1], idx[-1], len(order[order.index(idx[-1])+1:]),result)

            if "LIST" in original_prediction:
                if self.does_changes_prediction(op, result):
                    op = result

            else:

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
            test_split = test.split("[LIST]")

            return len(original_split) != len(test_split)
        else:
            return original != test

    def _generate_instances(self, surrogate_context, surrogate_query, surrogate_answer):
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

        if "[LIST]" in original_prediction:
            for i in range(5):
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
        else:

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
        return sorted_best, positive_samples, negative_samples
