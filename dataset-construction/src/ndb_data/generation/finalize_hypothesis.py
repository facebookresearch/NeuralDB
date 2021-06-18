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

import calendar
import json
import re
import pydash
from argparse import ArgumentParser
from itertools import product
from tqdm import tqdm
from wikidata_common.wikidata import Wikidata

unit_types = {}


def get_unit(unit_uri):
    if unit_uri in unit_types:
        return unit_types[unit_uri]
    unit_types[unit_uri] = wikidata.get_by_id_or_uri(unit_uri)
    return get_unit(unit_uri)


def check_match(snak, test):
    if snak is None or snak[0] is None:
        return False

    if "amount" in snak[0]:
        if snak[0]["amount"] == test:
            return True

        if "unit" in snak[0] and snak[0]["unit"] is not None and snak[0]["unit"] != "1":
            unit = get_unit(snak[0]["unit"])
            if f"{snak[0]['amount']} {unit['english_name']}" == test:
                return True

        return False
    else:
        if "time" in snak[0] and "precision" in snak[0]:

            matches = re.match(
                r"\+([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})([A-Za-z0-9+-:]+)",
                snak[0]["time"],
            )

            if matches is None:
                print(snak[0]["time"])
                return False

            if snak[0]["precision"] == 9:  # Year
                return matches.group(1) in test
            elif snak[0]["precision"] == 11:  # Year month date
                return (
                    matches.group(1) in test
                    and calendar.month_name[int(matches.group(2))] in test
                    and matches.group(3) in test
                )
            elif snak[0]["precision"] == 10:  # Year month
                return (
                    matches.group(1) in test
                    and calendar.month_name[int(matches.group(2))] in test
                )
            elif snak[0]["precision"] == 7:  # Century
                return matches.group(1)[:-2] in test
            elif snak[0]["precision"] == 8:  # Decade
                return matches.group(1)[:-1] in test

        print("*******")
        print(test)
        print(snak)
        print("*******")
        return False


if __name__ == "__main__":
    wikidata = Wikidata()
    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    args = parser.parse_args()
    added_hyps = 0
    dropped_hyps = 0
    with open(args.in_file) as f, open(args.out_file, "w+") as of:
        itr = tqdm(f)

        for idx, line in enumerate(itr):
            instance = json.loads(line)
            instance["valid_hypotheses"] = []

            for parse in instance["parses"]:
                all_subjects, all_relations, all_objects = parse

                if all_objects[1] == "numeric" or isinstance(all_objects[1], dict):
                    all_objects[1] = [all_objects[1]]

                hypotheses = product(all_subjects[1], all_relations[1], all_objects[1])
                for hypothesis in hypotheses:
                    s, r, o = hypothesis
                    objects = wikidata.find_custom(
                        "wikidata_id",
                        [
                            h
                            for h in hypothesis
                            if h != "numeric" or not isinstance(h, dict)
                        ],
                    )
                    objects_dict = {item["wikidata_id"]: item for item in objects}

                    try:
                        subject = objects_dict[s]
                        relation = objects_dict[r]
                    except Exception:
                        continue

                    # Retrieve all the (R,O) snaks for the given subject, filter by relation
                    subject_snaks = subject["properties"].get(
                        relation["wikidata_id"], []
                    )

                    if o == "numeric" or isinstance(o, dict):
                        o = all_objects[0]
                        # This checks whether this hypothesis exists in any of the retrieved snaks
                        if any(check_match(subj, o) for subj in subject_snaks):
                            added_hyps += 1
                            hypothesis = list(hypothesis)
                            hypothesis[2] = all_objects[0]
                            instance["valid_hypotheses"].append(hypothesis)
                        else:
                            dropped_hyps += 1

                    else:
                        object = objects_dict[o]
                        object_snaks = object["properties"].get(
                            relation["wikidata_id"], []
                        )
                        # Again, check whether the hypothesis snak exists in the list of retrieved snaks
                        if any(
                            pydash.get(subj[0], "id") == object["wikidata_id"]
                            for subj in subject_snaks
                        ) or any(
                            pydash.get(obj[0], "id") == subject["wikidata_id"]
                            for obj in object_snaks
                        ):
                            added_hyps += 1
                            instance["valid_hypotheses"].append(hypothesis)
                        else:
                            dropped_hyps += 1

            itr.desc = f"Line {idx}, Added {added_hyps}, dropped {dropped_hyps}"
            of.write(json.dumps(instance) + "\n")
