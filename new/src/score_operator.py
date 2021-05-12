import json
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
        return 1.0 if predicted[0] == actual[0] else 0.0

    elif query_type in {"argmin", "argmax", "set"}:
        return f1(set(actual if actual is not None else []),set(predicted if predicted is not None else []))

    elif query_type in {"count"}:
        if predicted is None or len(predicted) > 1:
            return 0.0

        return 1.0 if predicted[0] == actual[0] else 0.0
    elif query_type in {"bool"}:
        if predicted is None and actual is None:
            return 1.0
        else:
            if isinstance(actual, list) and isinstance(predicted, list):
                assert len(actual) == 1
                assert len(predicted) == 1
                return 1.0 if predicted[0] == actual[0] else 0.0

            return 0.0

    return 0.0


if __name__ == "__main__":
    breakdown_type = []
    raw = []

    with open("checkpoint/experiment=spj/db=v1.4_25,lr=1e-4/seed-1/metrics_test.json") as f:

        for line in f:
            instance = json.loads(line)["test"]
            raw.extend(instance["raw"])

    # by_db = defaultdict(list)
    # for i in raw:
    #     by_db[(i[3]['db_id'], i[3]["query_id"])].append(i)


    breakdown_type = defaultdict(list)
    breakdown_size = defaultdict(list)
    breakdown_rel = defaultdict(list)

    ss = defaultdict(list)
    total_scores = list()

    for i in range(0,21):
        breakdown_size[i]=[]

    for predicted,actual,scc,metadata in raw:
        if scc < 1:
            print(metadata[""])
            print(predicted, actual)
            print()
        predicted = parse(predicted)
        actual = parse(actual)

        local_score = single_score(actual, predicted, metadata["type"])
        breakdown_type[metadata["type"]].append(local_score)
        breakdown_rel[metadata["relation"][0]].append(local_score)

        ss[metadata["type"]].append(len(metadata["facts"]))
        breakdown_size[len(metadata["facts"]) if len(metadata["facts"]) < 20 else 20].append(local_score)
        total_scores.append(local_score)



        # if len(metadata["facts"]) == 4:
        #     print(local_score,metadata["question"],predicted, actual)
        #     print()

    print("By relation type")
    for k,v in breakdown_type.items():
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
    plt.bar(list(breakdown_type.keys()), list(np.mean(k) for k in breakdown_type.values()))
    plt.show()

    plt.title("Accuracy by relation")
    plt.bar(list(breakdown_rel.keys()), list(np.mean(k) for k in breakdown_rel.values()))
    plt.show()

    print()
    print("Total", np.mean(total_scores))
    print("Num instances", len(total_scores))
