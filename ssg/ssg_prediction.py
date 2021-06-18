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
import argparse
import json
import os

import numpy as np
import torch.nn as nn
from sentence_transformers import SentenceTransformer, util

from ssg_utils import read_NDB


def is_valid_folder(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="ssg predictions")
    parser.add_argument(
        "-i",
        dest="folder",
        required=True,
        help="input data folder",
        type=lambda x: is_valid_folder(parser, x),
    )
    parser.add_argument(
        "-m",
        dest="model_path",
        required=True,
        help="model folder",
        type=lambda x: is_valid_folder(parser, x),
    )

    parser.add_argument(
        "-th", dest="thresholds", type=float, nargs="+", help="thresholds", default=[0.8]
    )

    parser.add_argument("-b", dest="batch_size", type=int, help="batch size", default=100)

    parser.add_argument("-d", dest="device", default="cuda:0", help="output address")

    args = parser.parse_args()

    folder = args.folder
    batch_size = args.batch_size

    model_path = args.model_path
    device = args.device

    model = SentenceTransformer(model_path, device=device)

    thresholds = args.thresholds

    names = ["dev", "test"]

    softmax = nn.Softmax()
    for threshold in thresholds:
        for name in names:
            data_file = folder + "/" + name + ".jsonl"

            outfile = folder + "/" + name + "_" + str(threshold) + "_ssg_sup.json"
            dataset = read_NDB(data_file)
            ssg_data = []

            db_count = 0
            for d in dataset:

                questions = d[1]
                ctx = d[0]

                ctx.insert(0, "<eos>")
                ctx_reps = model.encode(ctx)
                q_count = 0
                for q in questions:

                    states = [[[-1, q["query"]]]]
                    new_states = []
                    final_sets = []
                    a_reps = ctx_reps[0: q["height"] + 2]

                    for t in range(2):

                        while states:
                            state = states.pop(0)

                            state_text = [s[1] for s in state]
                            s_text = ["[SEP]".join(state_text)]
                            s_reps = model.encode(s_text)

                            cos_scores = util.pytorch_cos_sim(s_reps, a_reps)[0]
                            cos_scores = cos_scores.cpu()

                            next_actions = np.nonzero(cos_scores > threshold).squeeze(1)

                            next_actions = next_actions.tolist()

                            if not next_actions:
                                st = state.copy()
                                final_sets.append(st[1:])

                            for a in next_actions:
                                if a == 0:
                                    st = state.copy()
                                    final_sets.append(st[1:])
                                else:
                                    pre_acts = [pre_act[0] for pre_act in state[1:]]
                                    if (a - 1) not in pre_acts:
                                        new_state = state.copy()
                                        new_state.append([a - 1, ctx[a]])
                                        new_states.append(new_state)
                        states = new_states
                        new_states = []

                    for s in states:
                        st = s.copy()
                        facts = st[1:]
                        if (
                            facts not in final_sets
                            and [facts[1], facts[0]] not in final_sets
                        ):
                            final_sets.append(st[1:])
                    data = {}
                    data["db_id"] = db_count
                    data["question_id"] = q_count
                    data["query"] = q["query"]
                    data["context_height"] = q["height"]
                    data["gold_facts"] = q["facts"]
                    data["answer"] = q["answer"]
                    data["metadata"] = {
                        "relation_type": q["relation"],
                        "query_type": q["type"],
                    }
                    data["ssg_output"] = final_sets

                    ssg_data.append(data)
                    q_count = q_count + 1

                db_count = db_count + 1

            with open(outfile, "w") as out_file:
                json.dump(ssg_data, out_file)
