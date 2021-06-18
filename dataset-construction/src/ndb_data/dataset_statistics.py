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
from collections import Counter


def merge_type(query_type):
    return query_type
    # .replace("arg", "")


def get_bool_ans(answers):
    return "NULL" if not len(answers) else ("TRUE" if "TRUE" in answers else "FALSE")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("in_file")
    args = parser.parse_args()

    type_counter = Counter()
    support_set_size_counter = Counter()
    bool_ans_counter = Counter()
    total_queries = 0
    total_dbs = 0
    with open(args.in_file) as f:

        for line in f:
            database = json.loads(line)
            for query in database["queries"]:

                support_set_size_counter[len(query["facts"])] += 1
                type_counter[merge_type(query["type"])] += 1

                if query["type"] == "bool":
                    bool_ans_counter[get_bool_ans(query["answer"])] += 1
            total_queries += len(database["queries"])
            total_dbs += 1

    for k, v in type_counter.items():
        print(k, v)

    print()
    for i in range(0, 20):
        print(i, support_set_size_counter[i])

    print(total_queries, total_dbs)
    print(bool_ans_counter)
