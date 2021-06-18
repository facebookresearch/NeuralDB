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
import logging

from neuraldb.dataset.instance_generator.instance_generator import InstanceGenerator

logger = logging.getLogger(__name__)


class WholeDBGenerator(InstanceGenerator):
    def _process_query(self, query_obj, update_tokens):
        query_tokens = self.tokenizer.tokenize(query_obj["query"])
        answer_tokens = [
            self.maybe_tokenize_answer(answer) for answer in query_obj["answer"]
        ]

        context_tokens = update_tokens[: query_obj["height"] + 1]

        yield self.maybe_decorate_with_metadata(
            {
                "query": query_tokens,
                "context": context_tokens,
                "output": self.concatenate_answer(answer_tokens),
            },
            query_obj,
        )
