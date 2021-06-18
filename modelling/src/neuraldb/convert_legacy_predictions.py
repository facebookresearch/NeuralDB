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

from functools import reduce

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    args = parser.parse_args()
    with open(args.in_file) as f, open(
        args.out_file,
        "w+",
    ) as of:
        for line in f:
            results = json.loads(line)
            for prediction in results["test"]["raw"]:
                predicted, actual, ems, eml, meta = prediction

                print(meta)

                instance = {
                    "prediction": predicted.split("[LIST]"),
                    "actual": actual.split("[LIST]"),
                    "metadata": {
                        "dbsize": len(
                            set(reduce(lambda a, b: a + b, meta["query"]["gold_facts"]))
                        )
                        if len(meta["query"]["gold_facts"])
                        else 0,
                        "type": meta["query"]["metadata"]["query_type"],
                    },
                }

                of.write(json.dumps(instance) + "\n")
