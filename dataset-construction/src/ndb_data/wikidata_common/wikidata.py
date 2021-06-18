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


class Wikidata(MongoDataSource):
    def __init__(self):
        super().__init__()
        self.collection = self.db["wiki_graph"]

    def get_by_id_or_uri(self, unit_uri):
        return self.collection.find_one(
            {"wikidata_id": unit_uri.replace("http://www.wikidata.org/entity/", "")}
        )

    def find_custom(self, search_key, search_toks):
        return self.collection.find({search_key: {"$in": search_toks}})

    def find_matching_relation(self, relation):
        return self.collection.find({"propery_types": relation})
