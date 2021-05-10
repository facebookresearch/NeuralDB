import logging
import json
import random
from argparse import ArgumentParser

from log_helper import setup_logging

logger = logging.getLogger(__name__)


def load_distractors(file):
    with open(file) as f:
        for line in f:
            yield line.strip()


if __name__ == "__main__":
    setup_logging()

    parser = ArgumentParser()
    parser.add_argument("--distractor-file", required=True)
    parser.add_argument("--in-file", required=True)
    parser.add_argument("--out-file", required=True)
    parser.add_argument("--num", type=int, required=True)
    args = parser.parse_args()

    distractors = list(load_distractors(args.distractor_file))

    with open(args.in_file) as f:
        dataset = json.load(f)

    for db in dataset:
        to_insert = random.sample(distractors, min(len(distractors), args.num))
        original_length = len(db["updates"])
        for distractor in to_insert:
            position = random.randint(0, len(db["updates"]))
            db["updates"].insert(position, [None, "distractor", distractor])

        mapping = dict()
        for idx, update in enumerate(db["updates"]):
            # Get the content of the update
            old_idx, type, text = update

            # Add the mapping if it was an original update
            if old_idx is not None:
                mapping[old_idx] = idx

            # Then set the idx to the new index
            update[0] = idx

        mapping[original_length] = len(db["updates"])

        for query in db["queries"]:
            # If the dataset is v0.4, we just update the context height.
            # If it's v0.5, we need to update the pointer to the naswer too

            query[0] = mapping[query[0]]
            if len(query) == 6:
                query[1] = [mapping[a] for a in query[1]]

    with open(args.out_file, "w+") as f:
        json.dump(dataset, f)
