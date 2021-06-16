import json
from argparse import ArgumentParser

from functools import reduce

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    args = parser.parse_args()
    with open(args.in_file) as f, open(
        args.out_file,
        "w+",
    ) as of:
        for line in f:
            results = json.loads(line)
            for prediction in results["test"]["raw"]:
                predicted, actual, ems, eml, meta = prediction

                print(meta)

                instance = {
                    "prediction": predicted.split("[LIST]"),
                    "actual": actual.split("[LIST]"),
                    "metadata": {
                        "dbsize": len(
                            set(reduce(lambda a, b: a + b, meta["query"]["gold_facts"]))
                        )
                        if len(meta["query"]["gold_facts"])
                        else 0,
                        "type": meta["query"]["metadata"]["query_type"],
                    },
                }

                of.write(json.dumps(instance) + "\n")
