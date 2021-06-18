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
from pymongo import UpdateOne
from tqdm import tqdm

from ndb_data.wikidata_common.wikidata import Wikidata


def write_updates(batch_update):
    bulks = []
    for k, v in batch_update:
        bulks.append(UpdateOne(k, v))

    collection.bulk_write(bulks)


if __name__ == "__main__":
    client = Wikidata()
    collection = client.collection

    batch_update = []

    num_ops = 0
    tqdm_iter = tqdm(
        collection.find({}, {"_id": 1, "sitelinks": 1}),
        total=collection.estimated_document_count(),
    )
    for i in tqdm_iter:
        if type(i["sitelinks"]) == dict:
            batch_update.append(
                (
                    {"_id": i["_id"]},
                    {"$set": {"sitelinks": list(i["sitelinks"].values())}},
                )
            )

        if len(batch_update) > 10000:
            write_updates(batch_update)
            batch_update = []
            num_ops += 1
            tqdm_iter.desc = f"Performed update {num_ops}"
