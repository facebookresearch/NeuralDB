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
import os
from abc import ABC

import pymongo


class MongoDataSource(ABC):
    def __init__(self):
        user = os.getenv("MONGO_USER", "")
        password = os.getenv("MONGO_PASSWORD", "")
        host = os.getenv("MONGO_HOST", "localhost")
        port = os.getenv("MONGO_PORT", "27017")
        db = os.getenv("MONGO_DB", "wikidata")

        client = pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:{port}")

        self.db = client[db]
