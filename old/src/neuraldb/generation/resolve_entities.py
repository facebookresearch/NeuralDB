import json
from collections import defaultdict
from multiprocessing.pool import ThreadPool

from qwikidata.linked_data_interface import get_entity_dict_from_api
from tqdm import tqdm


def get_name_from_web(id):
    try:
        downloaded = get_entity_dict_from_api(id)
        name = downloaded["labels"]["en"]["value"]
        aliases = set()
        found_types = list()

        if "P31" in downloaded["claims"]:
            found_types.extend(
                [
                    a["mainsnak"]["datavalue"]["value"]["id"]
                    for a in downloaded["claims"]["P31"]
                ]
            )

        aliases.add(downloaded["labels"]["en"]["value"])
        if "aliases" in downloaded and "en" in downloaded["aliases"]:
            aliases.update([a["value"] for a in downloaded["aliases"]["en"]])

        return id, name, aliases, found_types
    except:
        return id, None, None, None


if __name__ == "__main__":
    missing = set()
    names = defaultdict(lambda: None)
    types = defaultdict(lambda: None)

    with open("entity_names.jsonl") as f:
        for line in f:
            ent = json.loads(line)
            names[ent["key"]] = ent["value"]

    with open("entity_types.jsonl") as f:
        for line in f:
            ent = json.loads(line)
            types[ent["key"]] = ent["value"]

    with open("positive_data.jsonl") as f:
        for line in tqdm(f,desc="Reading"):
            instance = json.loads(line)

            if instance["subject"][0] == "Q" and (
                "name." + instance["subject"] not in names
                or instance["subject"] not in types
            ):
                missing.add(instance["subject"])

            if instance["object"][0] == "Q" and (
                "name." + instance["object"] not in names
                or instance["object"] not in types
            ):
                missing.add(instance["object"])

            if (
                "extra_subject" in instance
                and instance["extra_subject"][0] == "Q"
                and (
                    "name." + instance["extra_subject"] not in names
                    or instance["extra_subject"] not in types
                )
            ):
                missing.add(instance["extra_subject"])

            if (
                "extra_object" in instance
                and instance["extra_object"][0] == "Q"
                and (
                    "name." + instance["extra_object"] not in names
                    or instance["extra_object"] not in types
                )
            ):
                missing.add(instance["extra_object"])

    pool = ThreadPool(processes=100)
    for entity, name, aliases, found_types in tqdm(
        pool.imap(get_name_from_web, missing), total=len(missing)
    ):
        if name is not None:
            names["name." + entity] = name
            names["alias." + entity] = list(aliases)
            types[entity] = found_types

    # Write out the negative examples
    with open("entity_names.jsonl", "w+") as f:
        for k, v in tqdm(names.items(), desc="Writing entity names dict"):
            f.write(json.dumps({"key": k, "value": v}) + "\n")

    # Write out the negative examples
    with open("entity_types.jsonl", "w+") as f:
        for k, v in tqdm(types.items(), desc="Writing entity types"):
            f.write(json.dumps({"key": k, "value": v}) + "\n")
