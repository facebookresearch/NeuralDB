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
import random
import logging
from typing import List, Any, Dict

logger = logging.getLogger(__name__)


class NeuralDBParser:
    def __init__(self, max_queries=None):
        self._max_queries = max_queries

    def load_instances(self, database: Dict[str, List[Any]]):
        return self._load_instances(database)

    def _load_instances(self, database: Dict[str, List[Any]]):
        logger.debug("Loading updates")
        updates = map(self._read_update, database["facts"])

        logger.debug("Loading queries")
        queries = filter(
            lambda query: query is not None,
            map(self._read_query, self._maybe_sample(database["queries"])),
        )

        return {"updates": updates, "queries": queries, "metadata": {}}

    def _maybe_sample(self, queries: List[Any]):
        if self._max_queries is not None:
            queries = random.sample(queries, min(len(queries), self._max_queries))
        return queries

    def _read_update(self, update):
        return update

    def _read_query(self, query):
        answer, answer_type = self._process_answer(query["answer"])
        query["answer"] = answer
        query["answer_type"] = answer_type
        return query

        # return {
        #     "id": query["id"],
        #     "height": query["height"],
        #     "input": query["query"],
        #     "output": answer,
        #     "metadata": {
        #         "answer_type": answer_type,
        #         "original_instance": query
        #     }
        # }

    def _process_answer(self, answer):
        return answer, None
