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
import json
import random
from argparse import ArgumentParser
from collections import Counter, defaultdict

import numpy as np
from tqdm import tqdm

from ndb_data.construction.make_database_initial import normalize_subject
from ndb_data.wikidata_common.kelm import KELMMongo
from ndb_data.wikidata_common.wikidata import Wikidata


# This will only return S,R,O triples that match our templates
def generate_hypotheses(instance):
    for s, r, o in instance["valid_hypotheses"]:
        if r not in final_templates:
            continue
        yield (s, r, o)


# This goes through the instances and pulls in related facts for joins/complex Qs
def bring_extra_facts(instance, extra, additional_list, search_id, is_subj):
    # If it's subject, it's the first element of the tuple, if object it's the last.
    pid = 0 if is_subj else 2

    # Iterate through all found KELM-mapped instances.
    # Each relation contains a set of the relation IDs and valid hypotheses
    for found in extra:

        # If it's the same fact. skip
        if found["reference"] == instance["reference"]:
            continue

        # Check if the KELM instance contains a relation that's in the additional list
        filtered = list(
            filter(
                lambda hyp: hyp[pid] == search_id and hyp[1] in additional_list,
                found["valid_hypotheses"],
            )
        )

        if not any(filtered):
            continue

        # If we're adding duplicate facts, then we're undoing the need for joins. so skip
        if any([f in instance["valid_hypotheses"] for f in filtered]):
            continue

        yield found


if __name__ == "__main__":
    kelm = KELMMongo()
    wiki = Wikidata()
    global_obs = []

    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    parser.add_argument("--target-size", type=int)
    args = parser.parse_args()

    with open("configs/generate_v1.5.json") as f:
        final_templates = json.load(f)

    with open("configs/filter_subjects.json") as f:
        additional_subjects = json.load(f)

    with open("configs/filter_objects.json") as f:
        additional_objects = json.load(f)

    with open("configs/expand_objects.json") as f:
        extra_objects = json.load(f)

    with open("configs/expand_subject.json") as f:
        extra_subjects = json.load(f)

    original_for = defaultdict(list)
    extra_kelm_for = defaultdict(list)

    # Go through all databases in the input file
    with open(args.in_file) as f, open(args.out_file, "w+") as of:
        for line in tqdm(f):
            db = json.loads(line)
            local_obs = []

            # For all facts in the database
            for instance in tqdm(db):
                for hyp in instance["valid_hypotheses"]:
                    hyp = tuple(hyp)
                    subject_id, relation_id, object_id = hyp

                    # Find an extra subject
                    extra_subj = list(
                        kelm.find_entity_rel(
                            subject_id,
                            set(additional_subjects.get(relation_id, {}).keys()).union(
                                extra_subjects.get(relation_id, {}).keys()
                            ),
                        )
                    )

                    # Find an extra object
                    if object_id.startswith("Q"):
                        extra_obj = list(
                            kelm.find_entity_rel(
                                object_id,
                                set(
                                    additional_objects.get(relation_id, {}).keys()
                                ).union(extra_objects.get(relation_id, {}).keys()),
                            )
                        )
                    else:
                        extra_obj = []
                    #
                    # print(len(extra_subj), len(extra_obj))

                    # Bring facts for these extras
                    ex_s = bring_extra_facts(
                        instance,
                        extra_subj,
                        set(additional_subjects.keys()).union(extra_subjects.keys()),
                        subject_id,
                        True,
                    )
                    ex_o = bring_extra_facts(
                        instance,
                        extra_obj,
                        set(additional_objects.keys()).union(extra_objects.keys()),
                        object_id,
                        True,
                    )

                    for e in ex_s:
                        extra_kelm_for[hyp].append(e)

                    for e in ex_o:
                        extra_kelm_for[hyp].append(e)

                    modifiers = []
                    local_obs.append(hyp[1])
                    original_for[hyp].append(instance)

            global_obs.append(local_obs)
            target_size = args.target_size

            # Sample extra facts for a subset. limit to maximum of 1/3 of the size of the dataset
            extra_key = list(extra_kelm_for.keys())
            sampled_extra_facts = random.sample(
                extra_key, k=min(len(extra_key), target_size // 3)
            )

            sampled = []
            references = set()
            for f in sampled_extra_facts:
                sampled.extend(original_for[f])
                extra_item = random.choice(extra_kelm_for[f])
                sampled.append(extra_item)

            # Go through all retrieved facts.
            # First, deduplicate, then normalize the subjects, then add it to the DB
            duplicates = []
            for idx, sampled_fact in enumerate(sampled):
                if "fact" not in sampled_fact:
                    fact = sampled_fact["candidate"].strip()
                    for subj, rel, obj in sampled_fact["valid_hypotheses"]:
                        if obj == "numeric":
                            break

                        name = wiki.get_by_id_or_uri(subj)["english_name"]
                        fact = normalize_subject(name, fact)

                        if fact is None:
                            # print("Skipped as unparasable - subj")
                            break

                        if obj.startswith("Q"):
                            name = wiki.get_by_id_or_uri(obj)["english_name"]
                            fact = normalize_subject(name, fact)

                        if fact is None:
                            # print("Skipped as unparasable - obj")
                            break

                    sampled_fact["fact"] = fact
                    if fact is None or "⁇" in fact:
                        duplicates.append(idx)

                if sampled_fact["reference"] in references:
                    duplicates.append(idx)

                if sampled_fact["fact"] is None:
                    duplicates.append(idx)
                references.add(sampled_fact["reference"])

            # Delete duplicates
            duplicates = list(set(duplicates))
            for dup in sorted(duplicates, reverse=True):
                del sampled[dup]

            # Add unqiue extra facts
            others = []
            for item in db:
                if item["reference"] not in references:
                    others.append(item)
            sampled.extend(
                random.sample(others, k=min(len(others), target_size - len(sampled)))
            )

            # Remove object IDs from sampled
            for s in sampled:
                if "_id" in s:
                    del s["_id"]

            of.write(
                json.dumps(
                    {
                        "metadata": {"raw": sampled},
                        "facts": [f["fact"] for f in sampled],
                    }
                )
                + "\n"
            )

    rel_avgs = defaultdict(list)
    for observation in global_obs:
        ctr = Counter()
        ctr.update(observation)

        for k, v in ctr.items():
            rel_avgs[k].append(v)

    for k, v in rel_avgs.items():
        print(k, np.mean(v), np.std(v))
