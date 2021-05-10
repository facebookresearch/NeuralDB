import json
import random

import os

from tqdm import tqdm


def to_true_false(projection):
    if projection == "Yes":
        return "TRUE"
    elif projection == "No":
        return "FALSE"
    else:
        return projection


def generate_negative(query, facts):
    correct_facts = set(query[1])
    incorrect_facts = [
        fact
        for idx, fact in enumerate(facts)
        if idx not in correct_facts and idx < query[0]
    ]

    yield {
        "projection": None,
        "fact": [
            fact[2]
            for fact in random.sample(incorrect_facts, k=min(len(incorrect_facts), 3))
        ],
        "query": query[4],
        "type": query[3],
        "relation": query[2],
    }


def generate_singles(query, facts):
    needed = set(query[1])
    correct_facts = [fact for idx, fact in enumerate(facts) if idx in needed]

    yield {
        "projection": to_true_false(query[5]),
        "fact": [fact[2] for fact in correct_facts],
        "query": query[4],
        "type": query[3],
        "relation": query[2],
    }


if __name__ == "__main__":
    dataset = "test"

    generated = []
    with open("v0.5/{}_queries_last_50.json".format(dataset)) as f:
        everything = json.load(f)

        for db in tqdm(everything):
            facts = db["updates"]
            queries = db["queries"]

            for query in queries:
                if query[5] == "None":
                    generated.extend(generate_negative(query, facts))
                elif query[3] in {
                    "atomic_extractive",
                    "atomic_boolean",
                    "join_extractive",
                    "join_boolean",
                }:
                    generated.extend(generate_singles(query, facts))
                else:
                    pass

    os.makedirs("v2", exist_ok=True)
    with open("v2/extracted_{}.jsonl".format(dataset), "w+") as f:
        for i in generated:
            f.write(json.dumps(i) + "\n")
