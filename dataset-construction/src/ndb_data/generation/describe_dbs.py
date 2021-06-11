import json
import numpy as np
from collections import Counter


def read_databases(file):
    with open(file) as f:
        for line in f:
            instance = json.loads(line)
            yield instance


if __name__ == "__main__":

    null_answers = 0
    true_answers = 0
    zero_answers = 0
    other_answers = 0

    num_fact_used = []
    answer_sizes = []
    type_counter = Counter()
    for db in read_databases("generated_dbs.jsonl"):
        for query in db["queries"]:
            num_fact_used.append(len(query["facts"]))
            type_counter[query["type"]] += 1
            answer_sizes.append(len(query["answer"]))

            if None in query["answer"]:
                null_answers += 1
            elif len(query["answer"]) == 0:
                zero_answers += 1
            elif True in query["answer"]:
                true_answers += 1
            else:
                other_answers += 1
    print(np.mean(num_fact_used), np.mean(answer_sizes))
    print(type_counter)
    print(true_answers, null_answers, zero_answers, other_answers)
