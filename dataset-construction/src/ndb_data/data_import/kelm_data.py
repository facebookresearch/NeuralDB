import json
from argparse import ArgumentParser
from tqdm import tqdm

from ndb_data.wikidata_common.kelm import KELMMongo

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("kelm_file")
    args = parser.parse_args()

    client = KELMMongo()
    collection = client.collection

    batch = []
    insert_count = 0
    with open(args.kelm_file) as f:
        _tqdm_iter = tqdm(enumerate(f))

        for idx, line in _tqdm_iter:
            instance = json.loads(line)

            subjects = set()
            relations = set()
            for hypothesis in instance["valid_hypotheses"]:
                s, r, o = hypothesis
                if s.startswith("Q"):
                    subjects.add(s)

                if o is not None and not isinstance(o, dict) and o.startswith("Q"):
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
