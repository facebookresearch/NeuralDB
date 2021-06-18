#
# Copyright (c) 2021 Facebook, Inc. and its affiliates.
#
# This file is part of NeuralDB.
# See https://github.com/facebookresearch/NeuralDB for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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
