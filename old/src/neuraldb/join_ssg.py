import json
from argparse import ArgumentParser
from collections import defaultdict

import os

from neuraldb.scoring.r_precision import f1, precision, recall

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("split")
    parser.add_argument("top", type=int)
    parser.add_argument("--aggregation", action="store_true")
    args = parser.parse_args()
    precisions = []
    recalls = []
    lens = []
    with open(f"v0.5/{args.split}_queries_last_50.json") as f:
        db = json.load(f)

        for idx, database in enumerate(db):
            files = []
            for seed in range(1, 5 + 1):
                files.append(
                    open(
                        "/checkpoint/jth/neuraldb/ssg_new/{}_{}_{}_queries_last_50.json".format(
                            idx, seed, args.split
                        )
                    )
                )

            for query, *predictions in zip(database["queries"], *files):
                guessed = defaultdict(int)
                for prediction in predictions:
                    prediction = json.loads(prediction)
                    for a, score in prediction["guessed_evidence"]:
                        guessed[a] += score

                high = sorted(guessed.items(), key=lambda a: a[1], reverse=True)[
                    : args.top
                ]

                if query[5] != "None" and (
                    query[3] == "set" or query[3] == "min/max" or query[3] == "count"
                ):
                    lens.append(len(high))
                    precisions.append(precision(query[1], [h[0] for h in high]))
                    recalls.append(recall(query[1], [h[0] for h in high]))

                    query.append([h[0] for h in high])
                elif query[5] == "None":
                    query.append([])
                else:
                    query.append(None)

    if args.aggregation:
        os.makedirs(f"v0.5_ds2_with_aggr_top_{args.top}", exist_ok=True)
        with open(
            f"v0.5_ds2_with_aggr_top_{args.top}/{args.split}_queries_last_50.json", "w+"
        ) as f:
            json.dump(db, f)
    else:
        os.makedirs(f"v0.5_ds2_no_aggr_top_{args.top}", exist_ok=True)
        with open(
            f"v0.5_ds2_no_aggr_top_{args.top}/{args.split}_queries_last_50.json", "w+"
        ) as f:
            json.dump(db, f)

    p, r = sum(precisions) / len(precisions), sum(recalls) / len(precisions)
    print(p, r, 2 * p * r / (p + r), sum(lens) / len(lens))
