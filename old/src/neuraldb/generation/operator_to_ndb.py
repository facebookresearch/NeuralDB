import itertools
import json
import sys
from copy import copy

import numpy as np
from argparse import ArgumentParser
from collections import defaultdict
import random

from tqdm import tqdm


def unique_instances(instances):
    unique_groups = defaultdict(list)
    for i in instances:
        unique_groups[(i["prop"], i["subject"], i["object"])].append(i)

    ret = []
    for usvo, mixed in unique_groups.items():
        ret.append(random.choice(mixed))

    return ret


def extract_facts(unique):
    return [i["fact"] for i in unique]


def contains_value(v):
    try:
        int(v)
        return True
    except:
        try:
            float(v)
            return True
        except:
            return False


def parse_value(v):
    try:
        return int(v)
    except:
        return float(v)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    parser.add_argument("sample", type=int)
    args = parser.parse_args()

    query_facts = defaultdict(list)
    negatives_facts = defaultdict(list)

    with open(args.in_file) as f:
        for line in tqdm(f):
            instance = json.loads(line)
            if instance["projection"] is None:
                continue

            query_facts[instance["query"]].append(instance)

    query_keys = list(query_facts.keys())

    negative_instances = []
    postitive_instances = defaultdict(list)
    for query, facts in tqdm(query_facts.items()):

        added = []
        # sample_space = list(query_keys.difference({query}))
        while len(added) < len(facts):
            sampled_query = random.choice(query_keys)
            if sampled_query != query:
                added.append(copy(random.choice(query_facts[sampled_query])))

        for a in added:
            a["query"] = query
            a["projection"] = None
            a["type"] = "negative"

        negative_instances.extend(added)
        for fact in facts:
            postitive_instances[fact["type"]].append(fact)

    smallest = min([len(a) for a in postitive_instances.values()])

    everything = []

    for k, v in postitive_instances.items():
        everything.extend(random.sample(v, min(int(smallest * 1.25), len(v))))

    everything.extend(
        random.sample(
            negative_instances, min(int(smallest * 2.5), len(negative_instances))
        )
    )

    save = random.sample(
        everything,
        k=min(args.sample if args.sample else len(everything), len(everything)),
    )
    with open(args.out_file, "w+") as f:
        for query in tqdm(save):
            f.write(json.dumps(query) + "\n")
