import json
from argparse import ArgumentParser

import numpy as np
import matplotlib.pyplot as plt

from collections import defaultdict
def precision(actual, predicted):
    actual_set = set(actual)
    return (
        sum(1.0 for p in predicted if p in actual_set) / float(len(predicted))
        if len(predicted)
        else 1.0
    )


def recall(actual, predicted):
    if len(actual) == 0:
        return 1.0

    actual_set = set(actual)
    return (
        sum(1.0 for p in predicted if p in actual_set) / float(len(actual))
        if len(actual)
        else 1.0
    )


def f1(actual, predicted):
    pr = precision(actual, predicted)
    rec = recall(actual, predicted)

    return 2.0 * pr * rec / (pr + rec) if (pr + rec > 0.0) else 0.0


def parse(answer):
    if answer == "[NULL_ANSWER]":
        return None
    return [a.strip() for a in answer.split("[LIST]")]


def single_score(actual, predicted, query_type):
    if query_type in {"min", "max"}:
        if actual is None:
            return 1.0 if predicted == actual else 0.0
        elif predicted is None:
            return 0.0
        return 1.0 if predicted[0] == actual[0] else 0.0

    elif query_type in {"argmin", "argmax", "set"}:
        return f1(set(actual if actual is not None else []),set(predicted if predicted is not None else []))

    elif query_type in {"count"}:

        if actual is None:
            if predicted is None:
                return 1.0
            else:
                return 0.0
        if predicted is None or len(predicted) > 1:
            return 0.0

        return 1.0 if predicted[0] == actual[0] else 0.0
    elif query_type in {"bool"}:
        if predicted is None and actual is None:
            return 1.0
        else:
            if isinstance(actual, list) and isinstance(predicted, list):
                if len(actual) == 1 and len(predicted) == 1:
                    return 1.0 if predicted[0] == actual[0] else 0.0

            return 0.0

    return 0.0


def se(actual, predicted):
    if actual is None:
        return None
    if predicted is None and actual is not None:
        return int(actual[0])**2

    else:
        if predicted:
            try:
                return (int(actual[0])-int(predicted[0]))**2
            except:
                return int(actual[0])**2
        else:
            return int(actual[0])**2


if __name__ == "__main__":
    breakdown = []
    raw = []
    parser = ArgumentParser()
    parser.add_argument("predictions_file")
    args = parser.parse_args()
    with open(args.predictions_file) as f:

        for line in f:
            instance = json.loads(line)["test"]
            raw.extend(instance["raw"])

    breakdown = defaultdict(list)
    breakdown_size = defaultdict(list)

    ss = defaultdict(list)
    total_scores = list()

    for i in range(0,21):
        breakdown_size[i]=[]
    sqe = []
    for predicted,actual, _,_ ,metadata in raw:
        predicted = parse(predicted)
        actual = parse(actual)

        if metadata["query_type"] == "count":
           sqe.append(se(actual,predicted))
        local_score = single_score(actual, predicted, metadata["query_type"])
        breakdown[metadata["query_type"]].append(local_score)

        ss[metadata["query_type"]].append(len(metadata["query"]["gold_facts"]))
        breakdown_size[len(metadata["query"]["gold_facts"]) if len(metadata["query"]["gold_facts"]) < 20 else 20].append(local_score)
        total_scores.append(local_score)

        if len(metadata["query"]["gold_facts"]) == 4:
            print(local_score,metadata["query"]["input"],predicted, actual)
            print()

    print("By relation type")
    for k,v in breakdown.items():
        print(f"{k} score={round(np.mean(v),4)} len={len(v)} avg_support_set_size={round(np.mean(ss[k]),2)}")

    print()
    print("By support set size")


    for k,v in breakdown_size.items():
        print(f"{k if k<20 else '>20'} score={round(np.mean(v),4)} len={len(v)}")

    plt.title("Number of instances by support set size")
    plt.bar(list(breakdown_size.keys()),list(len(k) for k in breakdown_size.values()))
    plt.show()

    plt.title("Accuracy by support set size")
    plt.bar(list(breakdown_size.keys()), list(np.mean(k) for k in breakdown_size.values()))
    plt.show()

    plt.title("Accuracy by type")
    plt.bar(list(breakdown.keys()), list(np.mean(k) for k in breakdown.values()))
    plt.show()

    print()
    print("Total", np.mean(total_scores))
    print("Num instances", len(total_scores))

    non_null_counts = list(filter(lambda i: i is not None, sqe))

    print(f"Count error", np.mean(non_null_counts), np.std(non_null_counts))