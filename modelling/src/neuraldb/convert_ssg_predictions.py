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
