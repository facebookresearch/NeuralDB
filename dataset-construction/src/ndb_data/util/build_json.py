import glob
import csv
import json
from argparse import ArgumentParser
from collections import defaultdict

import re


def read_csv(f):
    next(f)
    reader = csv.DictReader(f)

    templates = defaultdict(set)

    for template in reader:

        if len(template["fact"]):
            templates["fact"].add(template["fact"])

        if len(template["bool"]):
            if template["bool_answer"].lower() in ["true", "t", "1", "yes", "y"]:
                templates["bool"].add((template["bool"], template["bool_answer"]))

        if len(template["set"]):
            templates["set"].add((template["set"], template["set_projection"]))

        if len(template["count"]):
            templates["count"].add((template["count"], template["count_projection"]))

        if len(template["min"]):
            templates["min"].add((template["min"], template["min_projection"]))

        if len(template["max"]):
            templates["max"].add((template["max"], template["max_projection"]))

        if len(template["argmin"]):
            templates["argmin"].add((template["argmin"], template["argmin_projection"]))

        if len(template["argmax"]):
            templates["argmax"].add((template["argmax"], template["argmax_projection"]))

        templates["_subject"] = "$s"
        templates["_object"] = "$o"

    return {k: list(v) if isinstance(v, set) else v for k, v in templates.items()}


def swap_so(statement):
    return statement.replace("$s", "$tmp_s").replace("$o", "$s").replace("$tmp_s", "$o")


def make_symmetric(k, templates):

    if not k.startswith("_"):
        out = []
        out.extend(templates)
        out.extend([(swap_so(t[0]), swap_so(t[1])) for t in templates if len(t) == 2])
        out.extend([swap_so(t) for t in templates if isinstance(t, str)])
        return out
    else:
        return templates


if __name__ == "__main__":
    print("Generate")
    parser = ArgumentParser()
    parser.add_argument("version")
    args = parser.parse_args()
    # Read all CSV files in dir
    files = glob.glob("configs/for_{}/*.csv".format(args.version))
    print(files)

    all_templates = {}
    for file in files:
        match = re.match(r".*(P[0-9]+).*", file)

        if match is not None:
            name = match.group(1)

            with open(file) as f:
                template = read_csv(f)

            if name in {"P47", "P26"}:
                all_templates[name] = {
                    prop: make_symmetric(prop, rules)
                    for prop, rules in template.items()
                }
            else:
                all_templates[name] = template

    with open("configs/generate_{}.json".format(args.version), "w+") as of:
        json.dump(all_templates, of, indent=4)
