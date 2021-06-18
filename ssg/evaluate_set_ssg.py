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


def find_matches(a_set, a_set_of_sets):
    exact = 0
    soft = 0
    found = False
    for s in a_set_of_sets:
        s_set = set(s)
        if a_set == s_set:
            exact = 1
            soft = 1
            found = True
            break
    if not found:
        for s in a_set_of_sets:
            s_set = set(s)
            if a_set <= s_set:
                soft = 1
                break

    return exact, soft


def evaluate_ndb_with_ssg(data_file):
    with open(data_file) as json_file:
        data = json.load(json_file)

    counter = 0

    Ps_soft = {}
    Rs_soft = {}

    Ps_exact = {}
    Rs_exact = {}

    C = {}

    for d in data:
        counter = counter + 1

        gold_facts = d["gold_facts"]
        ssg_output = [[f[0] for f in ss] for ss in d["ssg_output"]]

        # in some legacy versions we might have both [4,5] and [5,4] in the ssg output; we remove one.
        remove_lst = []
        for s in ssg_output:
            if (
                len(s) > 1
                and [s[1], s[0]] in ssg_output
                and [s[1], s[0]] not in remove_lst
            ):
                remove_lst.append(s)
        for r in remove_lst:
            ssg_output.remove(r)

        answer = d["answer"]
        q_type = d["metadata"]["query_type"]

        if "complex" in q_type:
            q_type = "join"
        if "arg" in q_type or "min" in q_type or "max" in q_type:
            q_type = "min/max"
        if q_type not in Ps_soft:
            P_soft = 0
            P_exact = 0
            R_soft = 0
            R_exact = 0
            c = 1
        else:
            P_soft = Ps_soft[q_type]
            R_soft = Rs_soft[q_type]
            P_exact = Ps_exact[q_type]
            R_exact = Rs_exact[q_type]
            c = C[q_type] + 1

        ssg_count = 0
        gold_count = 0
        total_soft = 0
        total_exact = 0

        # precision
        if len(ssg_output) == 0:
            total_soft = 1
            total_exact = 1
            ssg_count = 1

        for s in ssg_output:
            ssg_count = ssg_count + 1

            if s in gold_facts or len(s) == 0:
                total_soft = total_soft + 1
                total_exact = total_exact + 1
            else:
                if len(s) > 1 and [s[1], s[0]] in gold_facts:
                    total_soft = total_soft + 1
                    total_exact = total_exact + 1
                else:
                    for gold_s in gold_facts:

                        if set(gold_s) <= set(s):
                            total_soft = total_soft + 1
                            break

        P_soft = P_soft + total_soft / ssg_count
        P_exact = P_exact + total_exact / ssg_count

        total_exact = 0
        total_soft = 0

        # Recall
        if len(gold_facts) == 0 or answer == "None":
            total_soft = 1
            total_exact = 1
            gold_count = 1
        else:
            for g in gold_facts:
                gold_count = gold_count + 1
                exact, soft = find_matches(set(g), ssg_output)
                total_soft = total_soft + soft
                total_exact = total_exact + exact

        R_soft = R_soft + total_soft / gold_count
        R_exact = R_exact + total_exact / gold_count

        Ps_exact[q_type] = P_exact
        Rs_exact[q_type] = R_exact
        Ps_soft[q_type] = P_soft
        Rs_soft[q_type] = R_soft
        C[q_type] = c

    total_p_exact = 0
    total_r_exact = 0
    total_p_soft = 0
    total_r_soft = 0
    total_c = 0

    for t in Ps_exact:
        print(t + ":")
        print(Ps_exact[t] / C[t], Rs_exact[t] / C[t])
        print(Ps_soft[t] / C[t], Rs_soft[t] / C[t])
        total_c = total_c + C[t]
        total_r_exact = total_r_exact + Rs_exact[t]
        total_p_exact = total_p_exact + Ps_exact[t]
        total_r_soft = total_r_soft + Rs_soft[t]
        total_p_soft = total_p_soft + Ps_soft[t]

    print("total: ")
    print(total_p_exact / total_c, total_r_exact / total_c)
    print(total_p_soft / total_c, total_r_soft / total_c)


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ssg predictions evaluations")
    parser.add_argument(
        "-i",
        dest="predictions_file",
        required=True,
        help="predictions file",
        type=lambda x: is_valid_file(parser, x),
    )

    args = parser.parse_args()

    evaluate_ndb_with_ssg(args.predictions_file)
