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
import json
from argparse import ArgumentParser
from tqdm import tqdm

from ndb_data.wikidata_common.kelm import KELMMongo

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("kelm_file")
    args = parser.parse_args()

    client = KELMMongo()
    collection = client.collection

    batch = []
    insert_count = 0
    with open(args.kelm_file) as f:
        _tqdm_iter = tqdm(enumerate(f))

        for idx, line in _tqdm_iter:
            instance = json.loads(line)

            subjects = set()
            relations = set()
            for hypothesis in instance["valid_hypotheses"]:
                s, r, o = hypothesis
                if s.startswith("Q"):
                    subjects.add(s)

                if o is not None and not isinstance(o, dict) and o.startswith("Q"):
                    subjects.add(o)

                relations.add(r)

            instance["entities"] = list(subjects)
            instance["relations"] = list(relations)

            batch.append(instance)
            if len(batch) >= 5000:
                collection.insert_many(batch)
                batch = []
                insert_count += 1

                _tqdm_iter.desc = f"Insert batch {insert_count}"

    collection.insert_many(batch)
    client.close()
