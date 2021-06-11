import glob
import json
import os
from argparse import ArgumentParser

from tqdm import tqdm
from transformers import AutoTokenizer

if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained("t5-base")
    parser = ArgumentParser()
    parser.add_argument("in_dir")
    parser.add_argument("out_dir")
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    for file in glob.glob(args.in_dir + "/*"):
        with open(file) as f, open(
            args.out_dir + "/" + os.path.basename(file), "w+"
        ) as of:
            sizes = []
            for line in tqdm(f, desc=file):
                db = json.loads(line)
                tt = sum(len(tokenizer.tokenize(fact)) for fact in db["facts"])
                if tt < 900:
                    of.write(line)
