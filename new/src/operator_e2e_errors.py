import json
from argparse import ArgumentParser

import numpy as np
import matplotlib.pyplot as plt

from collections import defaultdict

from dataset_creation.generation.question_to_db import generate_answers


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
    return answer


def single_score(actual, predicted, query_type):
    if query_type in {"min", "max"}:
        if isinstance(predicted,list) and not isinstance(predicted,str):
            return 1.0 if predicted[0] == actual[0] else 0.0
        return 0.0
    elif query_type in {"argmin", "argmax", "set"}:
        return f1(set(actual if actual is not None else []),set(predicted if predicted is not None else []))

    elif query_type in {"count"}:
        if predicted is None or len(predicted) > 1:
            return 0.0

        if isinstance(predicted, list) and not isinstance(predicted, str):
            return 1.0 if predicted[0] == actual[0] else 0.0
        else:
            return 0.0
    elif query_type in {"bool"}:
        if predicted is None and actual is None:
            return 1.0
        else:
            if isinstance(actual, list) and isinstance(predicted, list):
                assert len(actual) == 1
                if len(predicted) > 1:
                    if len(set(predicted)) > 1:
                        # TODO fix
                        return 0.0
                # assert len(predicted) == 1
                return 1.0 if predicted[0] == actual[0] else 0.0

            return 0.0

    return 0.0


if __name__ == "__main__":
    breakdown = []
    raw = []

    parser = ArgumentParser()
    parser.add_argument("metrics_file")
    args = parser.parse_args()

    with open(args.metrics_file) as f:

        for line in f:
            instance = json.loads(line)["test"]
            raw.extend(instance["raw"])

    by_db = defaultdict(list)
    for i in raw:
        by_db[(i[3]['db_id'], i[3]["query_id"])].append(i)

    breakdown_rel = defaultdict(list)
    breakdown_type = defaultdict(list)
    breakdown_size = defaultdict(list)

    for i in range(1,21):
        breakdown_size[i] = []

    ss = defaultdict(list)
    total_scores = list()

    restored = []
    for k,v in by_db.items():

        try:
            derivations = []
            for a in v:
                derivations.extend([c.strip() for c in a[1].split("[LIST]")])
            target_derivations = [{"qid":v[0][3]['type'],"symmetric":"P47" in v[0][3]['relation'],"generated":{"derivation":a.split(maxsplit=1)[1]}} for a in derivations]
        except:
            continue

        try:

            predicted_derivations = [{"qid": v[0][3]['type'], "symmetric": "P47" in v[0][3]['relation'],
                                      "generated": {"derivation": a[0].split(maxsplit=1)[1]}} for a in v]
            pred = generate_answers("", v[0][3]['type'], predicted_derivations)
        except ValueError:
            print([a[0] for a in v])
            pred = ""
        except AssertionError:
            pred = ""
        except IndexError:
            pred = ""
        except TypeError:
            pred = ""

        try:
            target = generate_answers("", v[0][3]['type'], target_derivations)
            restored.append((pred, target, None, v[0][3]))
        except:
            continue


    for predicted,actual,_,metadata in restored:
        predicted = parse(predicted)
        actual = parse(actual)

        local_score = single_score(actual, predicted, metadata["type"])
        if local_score == 0:
            print(local_score)
            print(predicted,actual)
            print(metadata)
            print()
            print()
