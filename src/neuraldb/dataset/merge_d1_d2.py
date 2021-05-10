import json
import random
from collections import defaultdict
from copy import copy

import os

from neuraldb.dataset.convert_to_operator import generate_negative, generate_singles


def mkpl(query, negatives):
    i = copy(query)
    i["fact"] = [query["fact"]]

    if random.uniform(0, 10) > 3:
        to_add = round(random.uniform(1, 3))
        original = len(i["fact"])
        while len(i["fact"]) < original + to_add:
            chosen = random.choice(negatives)
            if chosen["query"] != i["query"]:
                i["fact"].append(chosen["fact"])

    return i


def mkng(query):
    i = copy(query)
    i["fact"] = []
    i["projection"] = None
    i["type"] = "negative2"
    return i


if __name__ == "__main__":

    question_types = defaultdict(list)

    dataset = "train"

    d1_questions = defaultdict(list)
    generated = []
    with open(
        "v0.5/{}_queries_last_50.json".format(dataset if dataset != "val" else "dev")
    ) as f:
        everything = json.load(f)

        for db in everything:
            facts = db["updates"]
            queries = db["queries"]

            for query in queries:
                if query[5] == "None":
                    xg = list(generate_negative(query, facts))
                    generated.extend(xg)
                    d1_questions[query[3]].extend(xg)

                elif query[3] in {
                    "atomic_extractive",
                    "atomic_boolean",
                    "join_extractive",
                    "join_boolean",
                }:
                    xg = list(generate_singles(query, facts))
                    generated.extend(xg)
                    d1_questions[query[3]].extend(xg)

                else:
                    pass

    avg = int(
        round(sum(len(a) for a in d1_questions.values()) / len(d1_questions) / 500.0)
        * 500
    )
    with open("generated_clean_{}_newsamples.jsonl".format(dataset)) as f:
        for idx, line in enumerate(f):
            instance = json.loads(line)
            # if instance["projection"] is None:
            #    continue

            question_types[instance["type"]].append(instance)

    argmax_breakdown = defaultdict(lambda: defaultdict(list))
    argmin_breakdown = defaultdict(lambda: defaultdict(list))
    set_breakdown = defaultdict(list)
    count_breakdown = defaultdict(list)

    for question_type, data in question_types.items():

        for item in data:
            answer = item["projection"]

            if question_type == "argmin":
                key, value = [a.strip() for a in answer.split("[SEP]")]
                argmin_breakdown[item["query"]][key].append((value, item))
            elif question_type == "argmax":
                key, value = [a.strip() for a in answer.split("[SEP]")]
                argmax_breakdown[item["query"]][key].append((value, item))
            elif question_type == "set":
                set_breakdown[item["query"]].append(item)
            elif question_type == "count":
                count_breakdown[item["query"]].append(item)

    for query in random.sample(question_types["set"], 2 * avg):
        generated.append(mkpl(query, question_types["negative"]))

    for query in random.sample(question_types["count"], 2 * avg):
        generated.append(mkpl(query, question_types["negative"]))

    for query in random.sample(question_types["argmin"], 2 * avg):
        generated.append(mkpl(query, question_types["negative"]))

    for query in random.sample(question_types["argmax"], 2 * avg):
        generated.append(mkpl(query, question_types["negative"]))

    for query in random.sample(question_types["negative"], 4 * avg):
        generated.append(mkpl(query, question_types["negative"]))

    for query in random.sample(question_types["set"], int(0.5 * avg)):
        generated.append(mkng(query))

    for query in random.sample(question_types["count"], int(0.5 * avg)):
        generated.append(mkng(query))

    for query in random.sample(question_types["argmin"], int(0.5 * avg)):
        generated.append(mkng(query))

    for query in random.sample(question_types["argmax"], int(0.5 * avg)):
        generated.append(mkng(query))

    for query in random.sample(question_types["negative"], int(0.5 * avg)):
        generated.append(mkng(query))

    random.shuffle(generated)

    print(len(generated))
    os.makedirs("v2.3_noisy", exist_ok=True)
    with open("v2.3_noisy/generated_clean_{}.jsonl".format(dataset), "w+") as f:
        for i in generated:
            f.write(json.dumps(i) + "\n")
