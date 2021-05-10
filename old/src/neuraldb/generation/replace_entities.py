import json
import re
import random
import itertools
import sys
from collections import defaultdict
from copy import deepcopy
from typing import List
import re
import emoji
from tqdm import tqdm


def add_replacements(instance, entity_id, entity):

    instance["fact"] = instance["fact"].replace(entity_id, entity).strip()
    instance["query"] = instance["query"].replace(entity_id, entity).strip()

    return instance


def add_canonical_replacement(instance, entity_id, entity):

    if instance["projection"] is not None:
        instance["projection"] = (
            instance["projection"].replace(entity_id, entity).strip()
        )

    return instance


def get_namesets(entities):
    a = [
        (aliases[item] if item in aliases else None) if item.startswith("Q") else item
        for item in entities
    ]
    return a


def populate(instance):

    entities = []
    entities.append(instance["subject"])
    entities.append(instance["object"])

    if "extra_subject" in instance and "extra_object" in instance:
        entities.append(instance["extra_subject"])
        entities.append(instance["extra_object"])

    primary = list([names[a] if a in names else None for a in entities])

    generated = []

    master_instance = deepcopy(instance)
    for key, canonical in zip(entities, primary):
        if key.startswith("Q") and canonical is not None:
            master_instance = add_replacements(master_instance, key, canonical)
            master_instance = add_canonical_replacement(master_instance, key, canonical)

    if not (
        len(re.findall("(Q[0-9]+)", master_instance["fact"]))
        or len(re.findall("(Q[0-9]+)", master_instance["query"]))
        or (
            master_instance["projection"] is not None
            and len(re.findall("(Q[0-9]+)", master_instance["projection"]))
        )
    ):
        generated.append(master_instance)

    return generated
    master_instance = deepcopy(instance)

    was_human = False
    for key, canonical in zip(entities, primary):
        if key.startswith("Q"):

            if key in humans and canonical is not None and " " in canonical:
                was_human = True
                canonical = canonical.split(" ")[0]
            master_instance = add_replacements(master_instance, key, canonical)
            master_instance = add_canonical_replacement(master_instance, key, canonical)

    if was_human and not (
        len(re.findall("(Q[0-9]+)", master_instance["fact"]))
        or len(re.findall("(Q[0-9]+)", master_instance["query"]))
        or (
            master_instance["projection"] is not None
            and len(re.findall("(Q[0-9]+)", master_instance["projection"]))
        )
    ):
        generated.append(master_instance)

    if True:
        return generated
    else:
        namesets = get_namesets(entities)
        if None in namesets:
            return []

        combos = list(
            filter(
                lambda combo: tuple(combo[:2]) != tuple(primary),
                itertools.product(*namesets),
            )
        )
        to_generate = random.sample(combos, k=min(len(combos), 4))

        for sub_entities in to_generate:
            work_instance = deepcopy(instance)

            for key, val, canonical in zip(entities, sub_entities, primary):
                if key.startswith("Q"):
                    work_instance = add_replacements(work_instance, key, val)
                    work_instance = add_canonical_replacement(
                        work_instance, key, canonical
                    )

            if (
                len(re.findall("(Q[0-9]+)", work_instance["fact"]))
                or len(re.findall("(Q[0-9]+)", work_instance["query"]))
                or (
                    work_instance["projection"] is not None
                    and len(re.findall("(Q[0-9]+)", work_instance["projection"]))
                )
            ):
                continue

            assert (
                work_instance["projection"] is None
                or len(re.findall("(Q[0-9]+)", work_instance["projection"])) == 0
            )
            assert len(re.findall("(Q[0-9]+)", work_instance["fact"])) == 0
            assert len(re.findall("(Q[0-9]+)", work_instance["query"])) == 0

            generated.append(work_instance)

        return generated


if __name__ == "__main__":
    missing = set()
    aliases = defaultdict(lambda: None)
    names = defaultdict(lambda: None)

    import re

    humans = set()
    with open("entity_types.jsonl") as f:
        for line in f:
            ent = json.loads(line)
            if "Q5" in ent["value"]:
                humans.add(ent["key"])

    with open("entity_names.jsonl") as f:
        for line in f:
            ent = json.loads(line)
            if ent["key"].startswith("alias."):
                aliases[ent["key"].replace("alias.", "")] = ent["value"]

            if ent["key"].startswith("name."):
                names[ent["key"].replace("name.", "")] = ent["value"]
                a: List = aliases[ent["key"].replace("name.", "")]
                if ent["value"] is not None and a is not None:

                    a.remove(ent["value"])

    completed = []
    subjects = set()

    for ent, alias in aliases.items():
        to_delete = []
        for a in alias:
            if names[ent] != a:
                if len(a) <= 2:
                    to_delete.append(a)
                elif all(character in emoji.UNICODE_EMOJI for character in a):
                    to_delete.append(a)

        for rem in to_delete:
            alias.remove(rem)

    with open("generated_data.jsonl") as f:
        for line in tqdm(f):
            instance = json.loads(line)

            if instance["subject"][0] == "Q":
                if instance["subject"] in names:
                    subjects.add(instance["subject"])

            generated_instances = populate(instance)
            completed.extend(filter(lambda i: i is not None, generated_instances))

    print("Shuffling")

    all_subjects = list(subjects)
    random.shuffle(all_subjects)

    train_subjects = set(all_subjects[: len(all_subjects) // 100 * 80])
    val_subjects = set(
        all_subjects[len(all_subjects) // 100 * 80 : len(all_subjects) // 100 * 90]
    )
    test_subjects = set(all_subjects[len(all_subjects) // 100 * 90 :])

    print("Writing")
    with open("generated_clean_train.jsonl", "w+") as f:
        for instance in tqdm(completed):
            if instance["subject"] in train_subjects:
                f.write(json.dumps(instance) + "\n")

    with open("generated_clean_val.jsonl", "w+") as f:
        for instance in tqdm(completed):
            if instance["subject"] in val_subjects:
                f.write(json.dumps(instance) + "\n")

    with open("generated_clean_test.jsonl", "w+") as f:
        for instance in tqdm(completed):
            if instance["subject"] in test_subjects:
                f.write(json.dumps(instance) + "\n")
