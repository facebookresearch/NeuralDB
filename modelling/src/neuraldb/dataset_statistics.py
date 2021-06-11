import logging
import json
from collections import defaultdict
import random

from datasets import tqdm

from neuraldb.dataset.neuraldb_parser import NeuralDBParser
from neuraldb.util.log_helper import setup_logging

logger = logging.getLogger(__name__)


def get_instances_from_file(file):
    parser = NeuralDBParser()

    with open(file) as f:
        for line in f:
            database = json.loads(line)
            yield from parser.load_instances(database)["queries"]


def get_bool_breakdown(answers):
    if len(answers) == 0:
        return "NULL"

    answer_str = " ".join(answers)

    if "TRUE" in answer_str:
        return "TRUE"

    elif "FALSE" in answer_str:
        return "FALSE"

    assert False, "malformed"


def get_file_stats(file, drop_argmax_chance=None):
    stats = defaultdict(lambda: defaultdict(int))
    for instance in tqdm(get_instances_from_file(file)):
        if drop_argmax_chance and instance["type"] in ["argmax", "argmin"]:
            if random.randint(0, 100) < drop_argmax_chance * 100:
                continue

        stats["type"][instance["type"]] += 1
        stats["relation"][instance["relation"]] += 1
        stats["num_support_sets"][len(instance["facts"])] += 1

        if instance["type"] == "bool":
            stats["bool_breakdown"][get_bool_breakdown(instance["answer"])] += 1

    return stats


if __name__ == "__main__":
    setup_logging()
    print()

    file = "resources/v2.1_25_big/train.jsonl"

    stats = get_file_stats(file, 0.8)

    print(stats)
