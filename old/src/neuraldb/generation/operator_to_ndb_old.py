import itertools
import json
import numpy as np
from argparse import ArgumentParser
from collections import defaultdict
import random

from tqdm import tqdm


def unique_instances(instances):
    unique_groups = defaultdict(list)
    for i in instances:
        unique_groups[(i["prop"], i["subject"], i["object"])].append(i)

    ret = []
    for usvo, mixed in unique_groups.items():
        ret.append(random.choice(mixed))

    return ret


def extract_facts(unique):
    return [i["fact"] for i in unique]


def contains_value(v):
    try:
        int(v)
        return True
    except:
        try:
            float(v)
            return True
        except:
            return False


def parse_value(v):
    try:
        return int(v)
    except:
        return float(v)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("in_file")
    args = parser.parse_args()

    query_facts = defaultdict(list)

    with open(args.in_file) as f:
        for line in tqdm(f):
            instance = json.loads(line)
            if instance["projection"] is None:
                continue

            query_facts[instance["query"]].append(instance)

    facts_to_add = set()
    queries_to_add = []
    answers_to_add = []
    for query, instances in tqdm(query_facts.items()):
        unique = unique_instances(instances)
        fax, metas = extract_facts(unique)
        facts_to_add.update()
        queries_to_add.extend(
            [
                (query, instance["type"], instance["projection"], instance["fact"])
                for instance in unique
            ]
        )

    facts_to_add = list(facts_to_add)
    facts_to_add_index = {fact: idx for idx, fact in enumerate(tqdm(facts_to_add))}
    q_a = []

    added = 0
    breakdown = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for query, query_type, answer, fact in tqdm(queries_to_add):
        if query_type in ["argmax", "argmin"]:
            key, value = [a.strip() for a in answer.split("[SEP]")]
            breakdown[query_type][query][key].append((value, facts_to_add_index[fact]))
        else:
            breakdown[query_type][query]["all"].append(
                (answer, facts_to_add_index[fact])
            )

        added += 1

    for question, answer_dict in breakdown["argmin"].items():
        argmax_val = None
        argmax_key = None
        argmax_fact = None
        evaluated = []
        for key, value in answer_dict.items():
            numerical_value = None
            records = None
            if all(contains_value(v[0]) for v in value):
                smallest_idx = np.argmin([parse_value(v[0]) for v in value])
                numerical_value = parse_value(value[smallest_idx][0])
                records = [value[smallest_idx][1]]
                evaluated.extend(v[1] for v in value)
            else:
                numerical_value = len(set(v[0] for v in value))
                records = [v[1] for v in value]
                evaluated.extend(records)

            if argmax_val is None or numerical_value < argmax_val:
                argmax_val = numerical_value
                argmax_key = key
                argmax_fact = records

        if argmax_val is not None:
            q_a.append(
                [
                    "argmin",
                    question,
                    argmax_key + " [SEP] " + str(argmax_val),
                    argmax_fact,
                    evaluated,
                ]
            )

    for question, answer_dict in breakdown["argmax"].items():
        argmax_val = None
        argmax_key = None
        argmax_fact = None
        evaluated = []
        for key, value in answer_dict.items():
            numerical_value = None
            records = None
            if all(contains_value(v[0]) for v in value):
                smallest_idx = np.argmax([parse_value(v[0]) for v in value])
                numerical_value = parse_value(value[smallest_idx][0])
                records = [value[smallest_idx][1]]
                evaluated.extend(v[1] for v in value)
            else:
                numerical_value = len(set(v[0] for v in value))
                records = [v[1] for v in value]
                evaluated.extend(records)

            if argmax_val is None or numerical_value > argmax_val:
                argmax_val = numerical_value
                argmax_key = key
                argmax_fact = records

        if argmax_val is not None:
            q_a.append(
                [
                    "argmax",
                    question,
                    argmax_key + " [SEP] " + str(argmax_val),
                    argmax_fact,
                    evaluated,
                ]
            )

    for question, answer_dict in breakdown["min"].items():
        argmax_val = None
        argmax_key = None
        argmax_fact = None
        evaluated = []
        for key, value in answer_dict.items():
            numerical_value = None
            records = None
            if all(contains_value(v[0]) for v in value):
                smallest_idx = np.argmin([parse_value(v[0]) for v in value])
                numerical_value = parse_value(value[smallest_idx][0])
                records = [value[smallest_idx][1]]
                evaluated.extend(v[1] for v in value)
            else:
                numerical_value = len(set(v[0] for v in value))
                records = [v[1] for v in value]
                evaluated.extend(records)

            if argmax_val is None or numerical_value < argmax_val:
                argmax_val = numerical_value
                argmax_key = key
                argmax_fact = records

        if argmax_val is not None:
            q_a.append(["min", question, str(argmax_val), argmax_fact, evaluated])

    for question, answer_dict in breakdown["max"].items():
        argmax_val = None
        argmax_key = None
        argmax_fact = None
        evaluated = []
        for key, value in answer_dict.items():
            numerical_value = None
            records = None
            if all(contains_value(v[0]) for v in value):
                smallest_idx = np.argmax([parse_value(v[0]) for v in value])
                numerical_value = parse_value(value[smallest_idx][0])
                records = [value[smallest_idx][1]]
                evaluated.extend(v[1] for v in value)
            else:
                numerical_value = len(set(v[0] for v in value))
                records = [v[1] for v in value]
                evaluated.extend(records)

            if argmax_val is None or numerical_value > argmax_val:
                argmax_val = numerical_value
                argmax_key = key
                argmax_fact = records

        if argmax_val is not None:
            q_a.append(["max", question, str(argmax_val), argmax_fact, evaluated])

    for question, answer_dict in breakdown["count"].items():
        evaluated = []
        count = []
        for key, value in answer_dict.items():
            numerical_value = None
            records = None
            if all(contains_value(v[0]) for v in value):
                count.extend([parse_value(v[0]) for v in value])
            else:
                numerical_value = len(set(v[0] for v in value))
                count.append(numerical_value)

            evaluated.extend(v[1] for v in value)

        if count:
            q_a.append(["count", question, str(sum(count)), None, evaluated])

    for question, answer_dict in breakdown["set"].items():
        evaluated = []
        items = set()
        for key, value in answer_dict.items():
            numerical_value = None
            records = None
            items.update(v[0] for v in value)
            evaluated.extend(v[1] for v in value)

        q_a.append(["set", question, list(items), None, evaluated])

    selected_questions = q_a
    selected_facts = list(set(itertools.chain(*[q[4] for q in selected_questions])))
    fact_dict = {v: idx for idx, v in enumerate(selected_facts)}

    negative_instances = []
    postitive_instances = []
    for question in tqdm(selected_questions):
        negative_instances.extend(
            {
                "fact": facts_to_add[f],
                "question": question[1],
                "answer": None,
                "type": question[0],
            }
            for f in random.sample(
                list(filter(lambda k: k not in question[4], fact_dict.keys())),
                len(question[4]),
            )
        )

        postitive_instances.extend(
            {
                "fact": facts_to_add[f],
                "question": question[1],
                "answer": None,
                "type": question[0],
            }
            for f in question[4]
        )
        print(len(negative_instances))

    with open("generated_all_test.json", "w+") as f:
        json.dump(
            [
                {
                    "updates": [
                        [idx, "relation", facts_to_add[id]]
                        for idx, id in enumerate(selected_facts)
                    ],
                    "queries": [
                        [
                            len(selected_facts),
                            [fact_dict[id] for id in q[4]],
                            "relation",
                            q[0],
                            q[1],
                            q[2],
                        ]
                        for q in selected_questions
                    ],
                }
            ],
            f,
            indent=4,
        )
