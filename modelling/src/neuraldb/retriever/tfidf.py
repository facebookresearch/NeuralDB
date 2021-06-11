import json
import logging
from argparse import ArgumentParser

import math
from drqascripts.retriever.build_tfidf_lines import OnlineTfidfDocRanker

from neuraldb.util.log_helper import setup_logging

logger = logging.getLogger(__name__)


class TFIDFRetriever:
    class RankArgs:
        def __init__(self):
            self.ngram = 2
            self.hash_size = int(math.pow(2, 24))
            self.tokenizer = "simple"
            self.num_workers = None
            self.max_sent = 50

    def __init__(self):
        self.args = self.RankArgs()

    def lookup(self, queries, facts):
        tfidf = OnlineTfidfDocRanker(self.args, facts)

        for query in queries:
            ids, scores = tfidf.closest_docs(query, self.args.max_sent)
            yield ids


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    args = parser.parse_args()

    setup_logging()
    tfidf = TFIDFRetriever()
    with open(args.in_file) as f, open(args.out_file, "w+") as of:
        for line in f:
            database = json.loads(line)

            facts = database["facts"]
            queries = [q["query"] for q in database["queries"]]

            for query, ids in zip(database["queries"], tfidf.lookup(queries, facts)):
                query["predicted_facts"] = [
                    list(filter(lambda idx: idx <= query["height"], ids))
                ]

            of.write(json.dumps(database) + "\n")
