import os
import json
from argparse import ArgumentParser

import pymongo
from tqdm import tqdm

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("kelm_file")
    args = parser.parse_args()

    user = os.getenv("MONGO_USER", "")
    password = os.getenv("MONGO_PASSWORD", "")
    host = os.getenv("MONGO_HOST", "localhost")
    port = os.getenv("MONGO_PORT", "27017")
    db = os.getenv("MONGO_DB", "wikidata")

    client = pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:{port}")

    db = client["wikidata"]
    collection = db["kelm"]

    batch = []
    insert_count = 0
    with open(args.kelm_file) as f:
        _tqdm_iter = tqdm(enumerate(f))

        for idx,line in _tqdm_iter:
            instance = json.loads(line)

            subjects = set()
            relations = set()
            for hypothesis in instance["valid_hypotheses"]:
                s,r,o = hypothesis
                if s.startswith("Q"):
                    subjects.add(s)

                if o is not None and not isinstance(o,dict) and o.startswith("Q"):
                    subjects.add(o)

                relations.add(r)

            instance["entities"] = list(subjects)
            instance["relations"] = list(relations)

            batch.append(instance)
            if len(batch) >= 5000:
                collection.insert_many(batch)
                batch = []
                insert_count += 1

                _tqdm_iter.desc = f"Insert batch {insert_count}"


    collection.insert_many(batch)
    client.close()