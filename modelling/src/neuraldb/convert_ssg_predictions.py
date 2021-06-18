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
import logging
from argparse import ArgumentParser
from collections import defaultdict

from neuraldb.util.log_helper import setup_logging

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    setup_logging()

    parser = ArgumentParser()
    parser.add_argument("predictions_file")
    parser.add_argument("output_file")
    parser.add_argument("--master_file", required=True)
    args = parser.parse_args()
    questions_answers = defaultdict(list)

    use_predicted_type = True
    master_file = args.master_file  # "resources/v2.1_25/test.jsonl"
    out_file = args.output_file  # "resources/v2.1_25/dev_ssg_predictions.jsonl"
    predictions_file = (
        args.predictions_file
    )  # "resources/v2.1_25/dev_0.76_st_ssg_sup.json"

    predicted_instances = {}
    with open(predictions_file) as f:
        predictions = json.load(f)
        for inst in predictions:
            predicted_instances[(inst["db_id"], inst["question_id"])] = inst

    with open(master_file) as f, open(out_file, "w+") as of:
        for db_idx, line in enumerate(f):
            database = json.loads(line)

            for q_idx, query in enumerate(database["queries"]):
                query["predicted_facts"] = [
                    [a[0] for a in b]
                    for b in predicted_instances[(db_idx, q_idx)]["ssg_output"]
                ]

            of.write(json.dumps(database) + "\n")
