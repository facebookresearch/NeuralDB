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
from ndb_data.wikidata_common.common_mongo import MongoDataSource


class KELMMongo(MongoDataSource):
    def __init__(self):
        super().__init__()
        self.collection = self.db["kelm"]

    def find_entity(self, entity):
        results = self.collection.find({"entities": entity})
        return results

    def find_entity_rel(self, entity, rels):
        results = self.collection.find(
            {"entities": entity, "relations": {"$in": list(rels)}}
        )
        return results
