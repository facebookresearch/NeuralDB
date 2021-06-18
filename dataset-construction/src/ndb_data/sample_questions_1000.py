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
import random
from collections import defaultdict

from argparse import ArgumentParser
from tqdm import tqdm


def get_size_bin(query):
    for idx, size in enumerate(size_bins):
        if len(query) <= size:
            return idx
    return len(size_bins)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    args = parser.parse_args()

    size_bins = [0, 1, 2, 4, 8, 12, 16, 20, 24]

    dataset = []
    added = 0

    db_sizes = defaultdict(int)

    added_q_type_bin = defaultdict(list)
    all_questions_binned = defaultdict(list)
    counts_bins = defaultdict(int)
    counts_facts = defaultdict(int)
    counts_types = defaultdict(int)

    complex_counts_bins = defaultdict(int)
    complex_counts_facts = defaultdict(int)
    complex_counts_types = defaultdict(int)

    with open(args.in_file) as f, open(args.out_file, "w+") as of:
        for db_idx, line in tqdm(enumerate(f)):
            instance = json.loads(line)
            instance["all_queries"] = instance["queries"]
            instance["queries"] = []

            for question_idx, question in enumerate(instance["all_queries"]):
                qrel = question["relation"]
                qtype = question["type"]
                qbin = get_size_bin(question["facts"])
                all_questions_binned[(qtype, qbin)].append((db_idx, question_idx))

    strata = list(all_questions_binned.keys())
    empty_bins = set()

    added_instances = []
    while len(empty_bins) < 0.75 * len(strata):
        key = random.choice(strata)

        if len(all_questions_binned[key]):
            # if key[1] < 3 and random.randint(0, 100) > 25:
            #     continue

            population = all_questions_binned[key]

            # Pop one from the population and add it to the dataset
            sample = population.pop(random.randint(0, len(population) - 1))
            added_q_type_bin[key].append(sample)
            instance["queries"].append(sample)
            added += 1
            added_instances.append(sample)
            counts_bins[key[1]] += 1

            if "complex" in question["id"] or "join" in question["id"]:
                complex_counts_bins[key[1]] += 1

        else:
            empty_bins.add(key)

    to_add = defaultdict(list)

    for db_idx, question_idx in added_instances:
        to_add[db_idx].append(question_idx)

    with open(args.in_file) as f, open(args.out_file, "w+") as of:
        for db_idx, line in tqdm(enumerate(f)):
            instance = json.loads(line)
            instance["all_queries"] = instance["queries"]
            instance["queries"] = []

            for question_idx, question in enumerate(instance["all_queries"]):
                if question_idx in to_add[db_idx]:

                    q_bin = get_size_bin(question["facts"])

                    # Filter weaker argmin/argmaxes
                    if question["type"] in {"argmin", "argmax", "min", "max"}:
                        #
                        if question["type"] == "argmin":
                            if random.random() < 0.6:
                                continue
                        else:

                            if (
                                len(question["answer"]) > 2
                                or len(question["derivations"]) == 1
                            ):
                                if random.random() < 0.95:
                                    continue
                            else:
                                if random.random() < 0.3:
                                    continue

                    #
                    if question["type"] == "bool" and "TRUE" in question["answer"]:
                        if random.random() < 0.3:
                            continue

                    # Less than 8 facts
                    if q_bin == 5:
                        # Drop half of the facts
                        if random.random() < 0.5:
                            continue

                    if q_bin == 4:
                        # Drop half of the facts
                        if random.random() < 0.5:
                            continue

                    if q_bin == 3:
                        # Drop half of the facts
                        if random.random() < 0.6:
                            continue

                    if q_bin == 2:
                        # Drop half of the facts
                        if random.random() < 0.9:
                            continue

                    if q_bin == 1:
                        # Drop 80% of the facts

                        if question["type"] == "bool":
                            if random.random() < 0:
                                continue

                        else:
                            if random.random() < 0.5:
                                continue

                    if q_bin == 0:
                        # Drop 90% of the facts
                        if random.random() < 0.5:
                            continue

                    if q_bin < 4:
                        if random.random() < 0.6:
                            continue

                    # if (
                    #     question["type"] == "bool"
                    #     and "FALSE" in question["answer"]
                    #     and random.randint(0, 100) > 55
                    # ):
                    #     continue
                    #
                    # if (
                    #     "complex" not in question["id"] and
                    #     question["type"] in {"argmax", "argmin"}
                    #     and random.randint(0, 100) > 30
                    # ):
                    #     continue
                    #
                    #
                    #
                    # if q_bin == 0 and random.randint(0, 100) > 30:
                    #     continue
                    # if (
                    #     question["type"] != "bool"
                    #     and q_bin == 1
                    #     and random.randint(0, 100) > 40
                    # ):
                    #     continue
                    # if (
                    #
                    #     question["type"] != "bool"
                    #     and q_bin == 2
                    #     and random.randint(0, 100) > 30
                    # ):
                    #     continue
                    # if q_bin == 3 and random.randint(0, 100) > 90:
                    #     continue
                    # if q_bin == 4 and random.randint(0, 100) > 9:
                    #     continue
                    # if q_bin == 5 and random.randint(0, 100) > 90:
                    #     continue
                    # if q_bin == 6 and random.randint(0, 100) > 90:
                    #     continue
                    # if q_bin == 7 and random.randint(0, 100) > 90:
                    #     continue
                    # if q_bin == 8 and random.randint(0, 100) > 90:
                    #     continue
                    counts_types[question["type"]] += 1
                    counts_facts[len(question["facts"])] += 1

                    if "complex" in question["id"] or "join" in question["id"]:
                        complex_counts_types[question["type"]] += 1
                        complex_counts_facts[len(question["facts"])] += 1

                    instance["queries"].append(question)
            del instance["all_queries"]

            if len(instance["queries"]):
                of.write(json.dumps(instance) + "\n")
                db_sizes[len(instance["queries"])] += 1

    for k, v in added_q_type_bin.items():
        print(k, len(v))
    print(added)
    # print(q_bin)
    # print(q_type)
    # print(q_type_bin)

    print("bins")
    for i in range(0, 9):
        print(i, counts_bins[i], complex_counts_bins[i])

    print("lens")
    for i in range(0, 26):
        print(i, counts_facts[i], complex_counts_facts[i])

    for k, v in counts_types.items():
        print(k, v, complex_counts_types[k])

    print(db_sizes)
