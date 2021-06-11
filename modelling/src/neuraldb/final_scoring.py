import glob
import json
from collections import OrderedDict, defaultdict

import numpy as np
import pandas as pd

from neuraldb.evaluation.scoring_functions import f1


def load_experiment(path):

    running_score = defaultdict(lambda: defaultdict(int))
    running_count = defaultdict(lambda: defaultdict(int))

    print(path)
    with open(path) as f:
        for line in f:
            instance = json.loads(line)
            actual = instance["actual"]
            prediction = instance["prediction"]

            local_score = f1(set(actual), set(prediction))

            # relation = instance["metadata"]["relation"]
            # running_score["relation"][relation] += local_score
            # running_count["relation"][relation] += 1

            qtype = instance["metadata"]["type"]
            if qtype in {"argmin", "argmax", "min", "max"}:
                qtype = "minmax"
            running_score["type"][qtype] += local_score
            running_count["type"][qtype] += 1

            running_score["all"][""] += local_score
            running_count["all"][""] += 1

    scores = {}
    for k, v in running_score.items():
        for attr, val in v.items():
            score = (
                running_score[k][attr] / running_count[k][attr]
                if running_count[k][attr]
                else 0
            )
            print(f"Running score: {k}\t{attr}\t\t{score}")
            scores["_".join([k, attr])] = (
                running_score[k][attr] / running_count[k][attr]
                if running_count[k][attr]
                else 0
            )

    return scores


if __name__ == "__main__":
    ndb_predictions = glob.glob("consolidated/work/v2.4_25/**/predictions.jsonl", recursive=True)
    all_experiments = []
    for prediction in ndb_predictions:
        print(prediction)

        experiment = OrderedDict()

        for element in prediction.split("/"):
            if "," in element:
                for kvp in element.split(","):
                    k, v = kvp.split("=", maxsplit=1)
                    experiment[k] = v
            elif "-" in element:
                for kvp in element.split(","):
                    k, v = kvp.split("-", maxsplit=1)
                    experiment[k] = v

        # experiment["ssg"] = prediction.replace(".jsonl", "").rsplit("_", maxsplit=1)[1]
        experiment["dataset"] = prediction.split("/")[2]
        if "retriever" not in experiment:
            experiment["retriever"] = ""
        experiment["path"] = prediction
        all_experiments.append(experiment)

    print("Reading by experiment: \n\n\n")
    for expt in all_experiments:
        expt.update(load_experiment(expt["path"]))
        del expt["path"]

    frame = pd.DataFrame(all_experiments)
    frame[frame.select_dtypes(include=['number']).columns] *= 100
    pd.set_option("display.width", 1000)
    pd.set_option("display.max_columns", None)

    aggr = {"all_": [np.mean, np.std]}
    aggr.update({k:[np.mean] for k in frame.columns if "type" in k})
    pt = pd.pivot_table(frame,index=["model","generator","retriever","lr", "steps"], aggfunc=aggr)
    print(pt)
