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
import logging
import random
from collections import defaultdict

import math
import numpy as np
from argparse import ArgumentParser
from nltk import ngrams
from nltk import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from similarity.normalized_levenshtein import NormalizedLevenshtein
from tqdm import tqdm

from ndb_data.util.log_helper import setup_logging

detok = TreebankWordDetokenizer()

logger = logging.getLogger(__name__)


def normalize_subject(subject_name, fact):
    if subject_name is None:
        return None

    skip = {"is", "a", "of", "between", "on", "in"}

    n = NormalizedLevenshtein()
    mixed_case_subject = not subject_name.islower()
    if mixed_case_subject and subject_name not in fact:
        toks = word_tokenize(fact)
        all_grams = []
        for i in range(1, len(toks)):
            all_grams.extend(" ".join(a) for a in ngrams(toks, i) if a[0] not in skip)

        scores = [n.similarity(gram, subject_name) for gram in all_grams]
        best_post = int(np.argmax(scores))

        original_subject_name = all_grams[best_post]
        if scores[best_post] < 0.5 or all_grams[best_post] == "name":
            return None

        fact = " ".join(toks)
        fact = fact.replace(original_subject_name, subject_name)
        fact = detok.detokenize(fact.split()).replace(" 's", "'s").replace(" ,", ",")

        if subject_name not in fact:
            return None

        assert subject_name in fact, f"Subject {subject_name} was not in {fact}"
    return fact


if __name__ == "__main__":
    setup_logging()
    parser = ArgumentParser()
    parser.add_argument("cache_dir")
    parser.add_argument("out_file")

    parser.add_argument("--num_dbs_to_make", type=int, default=50000)
    parser.add_argument("--sample_rels", type=int, default=4)
    parser.add_argument("--sample_per_rel", type=int, default=10)
    parser.add_argument("--sample_extra", type=int, default=5)
    args = parser.parse_args()

    loaded = []
    by_subject = defaultdict(list)
    by_object = defaultdict(list)
    by_relation = defaultdict(list)

    cache_files = glob.glob(args.cache_dir + "/*")
    for cache_file in cache_files:

        start_idx = len(loaded)
        with open(cache_file) as f:
            logger.info(f"Reading cache file {cache_file}")
            cache = json.load(f)
            loaded.extend(cache["loaded"])

            for subj, keys in cache["by_subject"].items():
                by_subject[subj].extend([k + start_idx for k in keys])

            for subj, keys in cache["by_object"].items():
                by_object[subj].extend([k + start_idx for k in keys])

            for subj, keys in cache["by_relation"].items():
                by_relation[subj].extend([k + start_idx for k in keys])

    all_subjects = list(by_subject.keys())
    all_relations = list(by_relation.keys())
    all_objects = list(by_object.keys())

    print(len(all_subjects), len(all_objects), len(all_relations))

    # Make train/dev/test split
    number_to_make = dict()
    number_to_make["train"] = args.num_dbs_to_make
    number_to_make["dev"] = max(5, args.num_dbs_to_make // 10)
    number_to_make["test"] = max(5, args.num_dbs_to_make // 10)

    all_entities = list(set(all_subjects).union(set(all_objects)))
    random.shuffle(all_entities)

    split_subjects = defaultdict(list)
    split_objects = defaultdict(list)
    split_by_relation = defaultdict(lambda: defaultdict(list))

    p1 = math.floor(len(all_entities) * 0.7)
    p2 = math.floor(len(all_entities) * 0.85)
    tr, de, te = all_entities[:p1], all_entities[p1:p2], all_entities[p2:]

    split_subjects["train"] = set([a for a in tr if a in by_subject])
    split_subjects["dev"] = set([a for a in de if a in by_subject])
    split_subjects["test"] = set([a for a in te if a in by_subject])

    split_objects["train"] = set([a for a in tr if a in by_object])
    split_objects["dev"] = set([a for a in de if a in by_object])
    split_objects["test"] = set([a for a in te if a in by_object])

    for split in ["train", "dev", "test"]:
        for rel, facts in by_relation.items():
            split_by_relation[split][rel].extend(
                [
                    f
                    for f in facts
                    if all(
                        h[0] in split_subjects[split]
                        for h in loaded[f]["valid_hypotheses"]
                    )
                    # and all(h[2] in split_objects[split] for h in loaded[f]['valid_hypotheses'])
                ]
            )
    print([(k, len(v)) for k, v in split_by_relation["train"].items()])
    print([(k, len(v)) for k, v in split_by_relation["dev"].items()])
    print([(k, len(v)) for k, v in split_by_relation["test"].items()])

    for split in ["train", "dev", "test"]:
        with open(args.out_file + "_" + split, "w+") as of:
            for db_id in tqdm(
                range(number_to_make[split]), total=number_to_make[split]
            ):
                # print(f"Building database {db_id}")

                new_db_fact_ids = set()

                db_subjs = random.sample(split_subjects[split], k=args.sample_extra)
                db_objs = random.sample(split_objects[split], k=args.sample_extra)
                db_rels = random.sample(all_relations, k=args.sample_rels)

                for fact in db_subjs:
                    new_db_fact_ids.update(by_subject[fact])

                for fact in db_objs:
                    new_db_fact_ids.update(by_object[fact])

                for rel in db_rels:
                    new_db_fact_ids.update(
                        random.sample(
                            split_by_relation[split][rel],
                            k=min(
                                len(split_by_relation[split][rel]), args.sample_per_rel
                            ),
                        )
                    )

                db = [loaded[idx] for idx in new_db_fact_ids]
                print(len(db))
                of.write(json.dumps(db) + "\n")
