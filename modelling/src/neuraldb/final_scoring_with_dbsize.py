import glob
import json
from collections import OrderedDict, defaultdict

import numpy as np
import pandas as pd

from neuraldb.evaluation.scoring_functions import f1
from functools import reduce


def load_experiment(path):

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
    master_file = "resources/v2.4_25/test.jsonl"

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

    ndb_predictions = glob.glob(
        "consolidated/work/v2.4_25/**/predictions.jsonl", recursive=True
    )
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

        if "spj" not in experiment["generator"] and experiment["steps"] == "1":
            continue

        all_experiments.append(experiment)

    print("Reading by experiment: \n\n\n")
    for expt in all_experiments:
        expt.update(load_experiment(expt["path"]))
        del expt["path"]

    original_frame = pd.DataFrame(all_experiments)
    pd.set_option("display.width", 1000)
    pd.set_option("display.max_columns", None)

    graph_keys = ["size_0", "size_1", "size_2-4", "size_5-9", "size_10-19"]

    aggr = {"all_": [np.mean, np.std]}
    aggr.update({k: [np.mean, np.std] for k in graph_keys})

    pt = pd.pivot_table(
        original_frame,
        index=["model", "generator", "lr", "steps"],
        aggfunc=aggr,
        fill_value=0,
    )
    frame = pd.DataFrame(pt.to_records())
    frame.columns = [
        hdr.replace("('all_', '", "all.")
        .replace("('size_", "size_")
        .replace(", ", ".")
        .replace(")", "")
        .replace("'", "")
        for hdr in frame.columns
    ]

    print(pt)
    final_configs = [
        ["t5", "1e-4", "spj"],
        ["t5", "1e-4", "perfectir"],
        ["longformer", "1e-4", "perfectir"],
        ["t5-fid", "1e-4", "perfectir"],
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
        for k in graph_keys:
            series.extend(
                frame[
                    (frame.model == model)
                    & (frame.lr == lr)
                    & (frame.generator == gene)
                ][k + ".mean"]
            )

            stds.extend(
                frame[
                    (frame.model == model)
                    & (frame.lr == lr)
                    & (frame.generator == gene)
                ][k + ".std"]
            )

        all_series.append(series)
        all_stds.append(stds)

    all_series[0][0] = 1.0
    all_stds[0][0] = 0.0

    for series, stds in zip(all_series, all_stds):
        ax.plot(series)
        ax.fill_between(
            range(len(series)),
            [min(1, s + i) for (s, i) in zip(series, stds)],
            [s - i for (s, i) in zip(series, stds)],
            alpha=0.4,
        )

    plt.xticks([0, 1, 2, 3, 4], labels=[k.replace("size_", "") for k in graph_keys])
    plt.xlabel("Number of support sets")
    plt.ylabel("Answer Accuracy")
    plt.legend(
        ["Neural SPJ", "T5", "Longformer", "FiD"], loc="lower left", fontsize="xxsmall"
    )  # "T5 FiD", "TF-IDF", "DPR"])
    # plt.tight_layout()
    # plt.show()
    plt.savefig("by_dbsize.pdf", bbox_inches="tight")

    # fig, ax = plt.subplots(figsize=(5, 3))
    #
    # pt = pd.pivot_table(original_frame, index=["model", "generator", "lr","retriever", "steps"], aggfunc=aggr, fill_value=0)
    #
    # frame = pd.DataFrame(pt.to_records())
    # frame.columns = [
    #     hdr.replace("('all_\', \'", "all.").replace("('size_", "size_").replace("('type_", "type_").replace(", ", ".").replace(")", "").replace(
    #         "\'", "") for hdr in frame.columns]
    #
    #
    # all_series = []
    # all_stds = []
    # final_configs = [
    #     # ["t5", "1e-4", "spj", "ssg"],
    #     ["t5", "1e-4", "spj_rand", "ssg"],
    #     ["t5", "1e-4", "externalir2", "tfidf"],
    #     ["t5", "1e-4", "externalir2", "dpr"],
    # ]
    # for model, lr, gener, retr in final_configs:
    #     print(model, lr, gener, retr)
    #     series = []
    #     stds = []
    #     for k in graph_keys:
    #         series.extend(
    #             frame[
    #                 (frame.model == model)
    #                 & (frame.lr == lr)
    #                 & (frame.generator == gener)
    #                 & (frame.retriever == retr)
    #             ][k+".mean"]
    #         )
    #
    #         stds.extend(
    #             frame[
    #                 (frame.model == model)
    #                 & (frame.lr == lr)
    #                 & (frame.generator == gener)
    #                 & (frame.retriever == retr)
    #                 ][k + ".std"]
    #         )
    #
    #
    #     all_series.append(series)
    #     all_stds.append(stds)
    #     print(series)
    #
    # # all_series[0][0] = 1.0
    #
    # for series,stds in zip(all_series,all_stds):
    #     ax.plot(series)
    #     ax.fill_between(range(len(series)),[min(1,s+i) for (s,i) in zip(series,stds)],[s-i for (s,i) in zip(series,stds)], alpha=0.4)
    #
    #
    #
    # plt.xticks([0, 1, 2, 3, 4], labels=[k.replace("size_", "") for k in graph_keys])
    # plt.xlabel("Query support set size")
    # plt.ylabel("Answer Exact Match")
    # plt.legend(["SSG+SPJ", "T5+TFIDF", "T5+DPR"])
    # # plt.tight_layout()
    # # plt.show()
    # plt.savefig("retr_dbsize.pdf", bbox_inches="tight")
