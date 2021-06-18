#
# Copyright (c) 2021 Facebook, Inc. and its affiliates.
#
# This file is part of NeuralDB.
# See https://github.com/facebookresearch/NeuralDB for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import itertools
import logging
import random
from copy import copy

from transformers import PreTrainedTokenizer

from neuraldb.dataset.instance_generator.instance_generator import InstanceGenerator

logger = logging.getLogger(__name__)


class NeuralSPJGenerator(InstanceGenerator):
    def __init__(
        self,
        tokenizer: PreTrainedTokenizer,
        maximum_source_length=256,
        maximum_target_length=64,
        padding=None,
        ignore_pad_token_for_loss=True,
        test_mode=False,
        **kwargs
    ) -> object:

        super().__init__(
            tokenizer,
            maximum_source_length,
            maximum_target_length,
            padding,
            ignore_pad_token_for_loss,
            test_mode,
        )

        self.question_types = {
            "set": "[SET]",
            "count": "[COUNT]",
            "bool": "[BOOL]",
            "argmax": "[ARGMAX]",
            "argmin": "[ARGMIN]",
            "min": "[MIN]",
            "max": "[MAX]",
        }

        for question_type in set(self.question_types.values()):
            self.tokenizer.add_tokens(question_type, special_tokens=False)

        self.only_allow_predictions = None
        self.sample_probability_add_negatives = 0.6
        self.sample_probability_add_nulls = 0.20
        self.augment_training = kwargs.get("augment_training", False)

    def _process_query(self, query_obj, update_tokens):
        query_tokens = self.tokenizer.tokenize(query_obj["query"])

        if "predicted_facts" in query_obj and self.test_mode:
            assert (
                self.only_allow_predictions is None
                or self.only_allow_predictions is True
            )
            if not self.only_allow_predictions:
                logger.warning("Using predicted facts")
            self.only_allow_predictions = True

            for fact_group in query_obj["predicted_facts"]:
                context_tokens = [update_tokens[fact] for fact in set(fact_group)]
                yield self.maybe_decorate_with_metadata(
                    {"query": query_tokens, "context": context_tokens},
                    query_obj,
                )

        # elif (
        #
        #     len(query_obj["facts"]) == 0 or len(query_obj["derivations"]) == 0
        # ) and query_obj["height"] > 2:
        #     assert (
        #         self.only_allow_predictions is None
        #         or self.only_allow_predictions is False
        #     )
        #     self.only_allow_predictions = False
        #
        #     population = list(set(range(query_obj["height"])))
        #
        #     negative = random.sample(
        #         population, k=min(len(population), random.randint(1, 3))
        #     )
        #
        #     # And also add the regular group
        #     context_tokens = [update_tokens[fact] for fact in negative]
        #     yield self.maybe_decorate_with_metadata(
        #         {
        #             "query": query_tokens,
        #             "context": context_tokens,
        #             "output": self._prepend_prediction_type_answer(
        #                 [self.null_answer_special], query_obj["type"]
        #             ),
        #         },
        #         query_obj,
        #     )

        else:
            assert (
                self.only_allow_predictions is None
                or self.only_allow_predictions is False
            )
            self.only_allow_predictions = False

            for fact_group, derivation in zip(
                query_obj["facts"], query_obj["derivations"]
            ):

                derivation_tokens = self.tokenizer.tokenize(derivation)

                # Augment with randomly sampled facts to simulate false positive instances from IR
                augmented_fact_group = copy(fact_group)
                if (
                    self.augment_training
                    and not self.test_mode
                    and random.uniform(0, 1) < self.sample_probability_add_negatives
                ):

                    # Make a list of all the facts for this query, and sample facts not in it
                    flat_facts = list(itertools.chain(*query_obj["facts"]))
                    population = list(
                        set(range(query_obj["height"])).difference(flat_facts)
                    )

                    # Add some of this negative evidence to the fact group
                    if len(population):
                        negative = random.sample(
                            population, k=min(len(population), random.randint(1, 3))
                        )
                        augmented_fact_group.extend(negative)
                        random.shuffle(augmented_fact_group)

                        # Add the augmented group
                        context_tokens = [
                            update_tokens[fact] for fact in augmented_fact_group
                        ]
                        yield self.maybe_decorate_with_metadata(
                            {
                                "query": query_tokens,
                                "context": context_tokens,
                                "output": self._prepend_prediction_type_answer(
                                    derivation_tokens, query_obj["type"]
                                ),
                            },
                            query_obj,
                        )

                if (
                    self.augment_training
                    and not self.test_mode
                    and random.uniform(0, 1) < self.sample_probability_add_nulls
                ):
                    # Make a list of all the facts for this query, and sample facts not in it
                    flat_facts = list(itertools.chain(*query_obj["facts"]))
                    population = list(
                        set(range(query_obj["height"])).difference(flat_facts)
                    )

                    # Add some of this negative evidence to the fact group
                    if len(population):
                        negative = random.sample(
                            population, k=min(len(population), random.randint(1, 3))
                        )

                        random.shuffle(negative)

                        # Add the augmented group
                        context_tokens = [update_tokens[fact] for fact in negative]
                        yield self.maybe_decorate_with_metadata(
                            {
                                "query": query_tokens,
                                "context": context_tokens,
                                "output": self._prepend_prediction_type_answer(
                                    [self.null_answer_special], query_obj["type"]
                                ),
                            },
                            query_obj,
                        )

                # And also add the regular group
                context_tokens = [update_tokens[fact] for fact in fact_group]
                yield self.maybe_decorate_with_metadata(
                    {
                        "query": query_tokens,
                        "context": context_tokens,
                        "output": self._prepend_prediction_type_answer(
                            derivation_tokens, query_obj["type"]
                        ),
                    },
                    query_obj,
                )

    def _prepend_prediction_type_answer(self, answer_tokens, answer_type):
        return [self.question_types[answer_type]] + answer_tokens
