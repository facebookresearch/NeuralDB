import glob
import json
import os

from tqdm import tqdm
from transformers import AutoTokenizer

if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained("t5-base")
    if os.path.exists("db_sizes.jsonl"):
        os.unlink("db_sizes.jsonl")

    for file in tqdm(glob.glob("dbs/*.jsonl")):
        with open(file) as f:
            sizes = []
            for line in f:
                db = json.loads(line)
                sizes.append(sum(len(tokenizer.tokenize(fact)) for fact in db["facts"]))

        with open("db_sizes.jsonl", "a+") as f:
            f.write(json.dumps({"file": file, "sizes": sizes}) + "\n")
            print(sizes)
