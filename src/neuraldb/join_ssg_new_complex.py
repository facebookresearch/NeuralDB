import json
from argparse import ArgumentParser
from collections import defaultdict

import os
from functools import reduce

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

    if not os.path.exists(f"resources/v1.8_25_ds_sg_{args.top}"):
        os.makedirs(f"resources/v1.8_25_ds_sg_{args.top}",exist_ok=True)
    with open(f"resources/v1.8_25/{args.split}.jsonl") as f, open(
            f"resources/v1.8_25_ds_sg_{args.top}/{args.split}.jsonl", "w+"
        ) as outf:

        for idx, line in enumerate(f):
            db = json.loads(line)


            files = []
            files.append(
                open(
                    "ssg_data/predictions_{}_{}".format(
                         args.split, idx
                    )
                )
            )

            for query, *predictions in zip(db["queries"], *files):
                guessed = defaultdict(int)
                for prediction in predictions:
                    prediction = json.loads(prediction)
                    for a, score in prediction["guessed_evidence"]:
                        guessed[a] += score

                query["predicted_evidence"] = []
                # high = sorted(guessed.items(), key=lambda a: a[1], reverse=True)[
                #     : args.top
                # ]

                high = prediction["guessed_evidence"][:args.top]

                lens.append(len(high))
                precisions.append(precision(reduce(lambda a,b:a+b, query["facts"]), [h[0] for h in high]))
                recalls.append(recall(reduce(lambda a,b:a+b, query["facts"]), [h[0] for h in high]))
                query["predicted_evidence"].extend([h[0] for h in high])


            outf.write(json.dumps(db)+"\n")

    p, r = sum(precisions) / len(precisions), sum(recalls) / len(precisions)
    print(p, r, 2 * p * r / (p + r), sum(lens) / len(lens))
