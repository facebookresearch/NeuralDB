import glob
import json
from collections import OrderedDict, defaultdict

import numpy as np
import pandas as pd

from neuraldb.evaluation.scoring_functions import f1
from functools import reduce


def load_experiment(path,db_sizes):

    running_score = defaultdict(lambda: defaultdict(int))
    running_count = defaultdict(lambda: defaultdict(int))

    print(path)
    with open(path) as f:
        for line in f:
            instance = json.loads(line)
            actual = instance["actual"]
            prediction = instance["prediction"]

            if "dbsize" not in instance["metadata"]:
                db_idx, q_idx = (
                    instance["metadata"]["database_idx"],
                    instance["metadata"]["question_idx"],
                )
                dbsize = db_sizes[(db_idx, q_idx)]
            else:
                dbsize = instance["metadata"]["dbsize"]

            if dbsize == 0:
                dbsize = "0"
            elif dbsize == 1:
                dbsize = "1"
            elif dbsize < 5:
                dbsize = "2-4"
            elif dbsize < 10:
                dbsize = "5-9"
            elif dbsize < 20:
                dbsize = "10-19"
            else:
                dbsize = "20+"

            local_score = f1(set(actual), set(prediction))

            # relation = instance["metadata"]["relation"]
            # running_score["relation"][relation] += local_score
            # running_count["relation"][relation] += 1

            qtype = instance["metadata"]["type"]
            if qtype in {"argmin", "argmax", "min", "max"}:
                qtype = "minmax"

            running_score["type"][qtype] += local_score
            running_count["type"][qtype] += 1

            running_score["size"][dbsize] += local_score
            running_count["size"][dbsize] += 1

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
    dbs = ["v2.4_25","v2.4_50","v2.4_100","v2.4_250","v2.4_500","v2.4_1000"]
    all_dbs = {}
    for file in dbs:
        master_file = f"resources/{file}/test.jsonl"

        db_sizes = dict()
        with open(master_file) as f:
            for db_idx, line in enumerate(f):
                database = json.loads(line)

                for q_idx, query in enumerate(database["queries"]):
                    db_sizes[(db_idx, q_idx)] = (
                        len(set(reduce(lambda a, b: a + b, query["facts"])))
                        if len(query["facts"])
                        else 0
                    )
        all_dbs[file] = db_sizes


    ndb_predictions = glob.glob("consolidated/work/*/**/predictions.jsonl", recursive=True)
    all_experiments = []
    for prediction in ndb_predictions:

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
        experiment["dataset"] = prediction.split("/")[2]
        experiment["path"] = prediction
        if experiment["generator"] == "spj_rand":
            experiment["retriever"] = "ssg"
        elif "retriever" not in experiment:
            experiment["retriever"] = ""

        all_experiments.append(experiment)

    print("Reading by experiment: \n\n\n")
    for expt in all_experiments:
        expt.update(load_experiment(expt["path"], all_dbs[expt["dataset"]]))
        del expt["path"]

    original_frame = pd.DataFrame(all_experiments)

    # original_frame[original_frame.select_dtypes(include=['number']).columns] *= 100

    pd.set_option("display.width", 1000)
    pd.set_option("display.max_columns", None)

    aggr = {"all_":[np.mean, np.std]}

    pt = pd.pivot_table(original_frame,index=["dataset","model","generator","retriever","lr", "steps"], aggfunc=aggr,fill_value=0)
    frame = pd.DataFrame(pt.to_records())
    frame.columns = [hdr.replace("('all_\', \'", "all.").replace("('size_","size_").replace(", ",".").replace(")", "").replace("\'","") for hdr in frame.columns]

    print(pt)
    final_configs = [
        ["t5", "1e-4", "spj"],
        ["t5", "1e-4", "spj_rand"],
        # ["longformer", "1e-4", "perfectir"],
        # ["t5-fid", "1e-4", "perfectir"],
    ]  # ,["t5-fid-max1","1e-4","perfectir"],]

    import matplotlib.pyplot as plt

    plt.style.use("ggplot")
    fig, ax = plt.subplots(figsize=(5, 3))

    all_series = []
    all_stds = []
    for model, lr, gene in final_configs:
        print(model, lr, gene)
        series = []
        stds = []
        for db in dbs:
            k = "all"
            series.extend(
                frame[
                    (frame.model == model)
                    & (frame.lr == lr)
                    & (frame.generator == gene)
                    & (frame.dataset == db)
                ][k+".mean"]
            )

            stds.extend(
                frame[
                    (frame.model == model)
                    & (frame.lr == lr)
                    & (frame.generator == gene)
                    & (frame.dataset == db)
                    ][k + ".std"]
            )

        all_series.append(series)
        all_stds.append(stds)

    final_configs = [
        # ["t5", "1e-4", "externalir", "tfidf"],
        # ["t5", "1e-4", "externalir", "dpr"],
        ["t5", "1e-4", "externalir2", "tfidf"],
        ["t5", "1e-4", "externalir2", "dpr"]
    ]
    for model, lr, gene, retr in final_configs:
        print(model, lr, gene)
        series = []
        stds = []
        for db in dbs:
            k = "all"

            print(frame[
                    (frame.model == model)
                    & (frame.lr == lr)
                    & (frame.generator == gene)
                    & (frame.retriever == retr)
                    & (frame.dataset == db)
                    ])
            series.extend(
                frame[
                    (frame.model == model)
                    & (frame.lr == lr)
                    & (frame.generator == gene)
                    & (frame.retriever == retr)
                    & (frame.dataset == db)
                ][k+".mean"]
            )

            stds.extend(
                frame[
                    (frame.model == model)
                    & (frame.lr == lr)
                    & (frame.generator == gene)
                    & (frame.retriever == retr)
                    & (frame.dataset == db)
                    ][k + ".std"]
            )

        if len(series) > 6:
            all_series.append(series[1:])
            all_stds.append(stds[1:])
        else:
            all_series.append(series)
            all_stds.append(stds)

    for series,stds in zip(all_series, all_stds):
        print(series)
        ax.plot(series)
        ax.fill_between(range(len(series)),[min(1,s+i) for (s,i) in zip(series,stds)],[s-i for (s,i) in zip(series,stds)], alpha=0.4)


    plt.xticks(range(len(dbs)), labels=[k.replace("v2.4_", "") for k in dbs])
    plt.xlabel("Number of facts in DB")
    plt.ylabel("Answer Accuracy")
    plt.legend(["SPJ PerfectIR","SSG+SPJ","T5 + TF-IDF","T5 + DPR"]  # "T5 FiD", "TF-IDF", "DPR"])
    , loc="lower left", fontsize="x-small")
    # plt.tight_layout()
    # plt.show()
    plt.savefig("ssg_dbsize.pdf", bbox_inches="tight")
