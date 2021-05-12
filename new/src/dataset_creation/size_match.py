import json
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("db1")
    parser.add_argument("db2")
    args = parser.parse_args()

    db1_query_count = 0
    with open(args.db1) as f:
        for line in f:
            instance = json.loads(line)
            db1_query_count += len(instance["queries"])

    db2_query_count = 0
    with open(args.db2) as f:
        for idx,line in enumerate(f):
            db2_query_count += len(instance["queries"])
            print(db1_query_count, db2_query_count, idx)

