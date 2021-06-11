import json
import logging
from argparse import ArgumentParser
from collections import defaultdict, Counter
from functools import reduce
from operator import itemgetter

from transformers import AutoTokenizer

from neuraldb.dataset.instance_generator.instance_generator import InstanceGenerator
from neuraldb.util.log_helper import setup_logging
from neuraldb.evaluation.scoring_functions import f1
import numpy as np

logger = logging.getLogger(__name__)


def extract_operator(prediction):
    prediction = prediction.replace("][NULL_ANSWER]", "] [NULL_ANSWER]")
    return prediction.split(maxsplit=1)[0].replace("[", "").replace("]", "").lower()


def majority_vote(predicted_types):
    ctr = Counter(predicted_types)
    return ctr.most_common(1)[0][0] if len(predicted_types) else "null"


def maybe_split_qtype(derivation):
    if derivation.strip().startswith("[") and derivation.strip().split()[0] not in {
        InstanceGenerator.empty_list_answer_special,
        InstanceGenerator.yes_answer_special,
        InstanceGenerator.no_answer_special,
        InstanceGenerator.null_answer_special,
        InstanceGenerator,
    }:
        bits = derivation.split(maxsplit=1)
        return bits[1].strip() if len(bits) > 1 else derivation.strip()

    return derivation.strip()


def try_numeric(item):
    item = item.replace("percent", "").strip()
    item = item.replace("trainset", "").strip()
    item = item.replace("tonne", "").strip()
    item = item.replace("kg", "").strip()
    item = item.replace("gramme", "").strip()
    item = item.replace("kilogramme", "").strip()
    item = item.replace("metre", "").strip()
    item = item.replace("kilometre", "").strip()
    item = item.replace("pound", "").strip()
    item = item.replace("ounce", "").strip()

    try:
        _ = int(item)
        return True
    except Exception:

        try:
            _ = float(item)
            return True
        except Exception:
            return False


def convert_comparable(item):
    if try_numeric(item):
        item = item.replace("percent", "").strip()
        item = item.replace("trainset", "").strip()
        item = item.replace("tonne", "").strip()
        item = item.replace("kg", "").strip()
        item = item.replace("gramme", "").strip()
        item = item.replace("kilogramme", "").strip()
        item = item.replace("metre", "").strip()
        item = item.replace("kilometre", "").strip()
        item = item.replace("pound", "").strip()
        item = item.replace("ounce", "").strip()

        return float(item.replace("numeric", ""))
    else:
        return item


def read_questions_into_dict(questions_file):
    questions = defaultdict(list)
    with open(questions_file) as f:
        for line in f:
            instance = json.loads(line)
            questions[instance["qid"]].append(instance)
    return questions


def maybe_split(keys):
    split = keys.split("[SEP]")
    if len(split) == 2:
        return split[0].strip(), split[1].strip(), None
    elif len(split) == 3:
        return [s.strip() for s in split]
    else:
        print(keys)


def generate_answers(question_type, question_facts):
    answer_keys = dict()
    if question_type == "argmin":
        # get all keys and find the key with the smallest count
        answers = defaultdict(list)
        numeric_answers = False
        for question in question_facts:
            if question["symmetric"]:
                ak = None
                question["generated"]["derivation"] = question["generated"][
                    "derivation"
                ].replace("[SEP]", "[SYM]")
                k, v = question["generated"]["derivation"].split("[SYM]")
            else:
                k, v, ak = maybe_split(question["generated"]["derivation"])
            assert "[SEP]" not in k
            assert "[SEP]" not in v

            if try_numeric(v):
                numeric_answers = True

            answers[k.strip()].append((convert_comparable(v.strip()), question))
            answer_keys[k.strip()] = ak

            if question["symmetric"]:
                answers[v.strip()].append((convert_comparable(k.strip()), question))

        if not len(answers):
            return [None]
        else:
            if not numeric_answers:
                best = sorted(answers.items(), key=lambda a: len(a[1]), reverse=False)
                lowest = len(best[0][1])
                best_answers = {k: v for k, v in best if len(v) == lowest}
            else:
                if len(set(type(a[1][0][0]) for a in answers.items())) > 1:
                    print(question)
                    print([a[1][0][0] for a in answers.items()])
                best = sorted(answers.items(), key=lambda a: a[1][0][0], reverse=False)
                lowest = best[0][1][0]
                best_answers = {k: v for k, v in best if v[0] == lowest}
            return list(
                [
                    answer_keys[k]
                    if k in answer_keys and answer_keys[k] is not None
                    else k
                    for k in best_answers.keys()
                ]
            )

    elif question_type == "argmax":
        # get all keys and find the key with the smallest count
        answers = defaultdict(list)

        numeric_answers = False
        for question in question_facts:
            if question["symmetric"]:
                ak = None
                question["generated"]["derivation"] = question["generated"][
                    "derivation"
                ].replace("[SEP]", "[SYM]")
                k, v = question["generated"]["derivation"].split("[SYM]")
            else:
                k, v, ak = maybe_split(question["generated"]["derivation"])
            assert "[SEP]" not in k
            assert "[SEP]" not in v

            if try_numeric(v):
                numeric_answers = True

            answers[k.strip()].append((convert_comparable(v.strip()), question))
            answer_keys[k.strip()] = ak

            if question["symmetric"]:
                answers[v.strip()].append((convert_comparable(k.strip()), question))

        if not len(answers):
            return [None]
        else:
            if not numeric_answers:
                best = sorted(answers.items(), key=lambda a: len(a[1]), reverse=True)
                highest = len(best[0][1])
                best_answers = {k: v for k, v in best if len(v) == highest}
            else:
                if len(set(type(a[1][0][0]) for a in answers.items())) > 1:
                    logger.warning(question)
                    logger.warning([a[1][0][0] for a in answers.items()])
                best = sorted(answers.items(), key=lambda a: a[1][0][0], reverse=True)
                highest = best[0][1][0]
                best_answers = {k: v for k, v in best if v[0] == highest}
            return list(
                [
                    answer_keys[k]
                    if k in answer_keys and answer_keys[k] is not None
                    else k
                    for k in best_answers.keys()
                ]
            )

    elif question_type == "min":
        # get all keys and find the key with the smallest count
        answers = []

        for question in question_facts:
            v = question["generated"]["derivation"]
            if "[SEP]" in v:
                v = v.split("[SEP]", maxsplit=1)[1].strip()

            assert "[SEP]" not in v, v

            assert try_numeric(v)
            answers.append(convert_comparable(v))

        best = np.min(answers) if len(answers) else None
        return [best]

    elif question_type == "max":
        # get all keys and find the key with the smallest count
        answers = []

        for question in question_facts:
            v = question["generated"]["derivation"]
            if "[SEP]" in v:
                v = v.split("[SEP]", maxsplit=1)[1].strip()

            assert "[SEP]" not in v, v
            answers.append(convert_comparable(v))

        best = np.max(answers) if len(answers) else None
        return [best]

    elif question_type == "count":
        # get all keys and find the key with the smallest count
        answers = set()

        for question in question_facts:
            v = question["generated"]["derivation"]
            assert "[SEP]" not in v, v
            answers.add(convert_comparable(v))

        best = len(answers)
        return [best]

    elif question_type == "bool":
        # get all keys and find the key with the smallest count
        answers = set()

        for question in question_facts:
            v = question["generated"]["derivation"]
            assert "[SEP]" not in v, v
            assert v == "TRUE" or v == "FALSE"
            answers.add(convert_comparable(v))

        return list(answers) if len(answers) else [None]

    elif question_type == "set":
        answers = set()

        for question in question_facts:
            v = question["generated"]["derivation"]
            assert "[SEP]" not in v, v
            answers.add(convert_comparable(v))

        return list(answers)

    raise Exception("Unknown quesiton type")


def linearize(pos):
    return (pos[0], tuple(pos[1]))


def process_lists(derivation: str, qtype: str):
    if "[LIST]" not in derivation:
        return [derivation]

    bits = derivation.split("[LIST]")
    if len(set(b.count("[SEP]") for b in bits)) == 1:
        return bits
    else:
        first_bit = derivation.rsplit("[SEP]", maxsplit=1)[0].strip()
        return [bits[0]] + [
            (first_bit + "[SEP] " + b.strip()).strip() for b in bits[1:]
        ]


def post_process_instances(instances, use_predicted_type=True):
    predicted_types = list(map(itemgetter("predicted_type"), instances))
    new_instance = {
        "metadata": instances[0]["metadata"],
        "predicted_type": majority_vote(predicted_types),
    }

    if new_instance["predicted_type"] == "null":
        logger.error(instances)

    derivations = list(
        filter(
            lambda inst: "NULL_ANSWER" not in inst,
            reduce(lambda a, b: a + b, map(itemgetter("prediction"), instances)),
        )
    )
    derivations = (
        reduce(
            lambda a, b: a + b,
            map(
                lambda derv: derv.split("[LIST]"),
                map(maybe_split_qtype, set(derivations)),
            ),
        )
        if len(derivations)
        else []
    )
    derivations = list(derivations)

    try:
        pred_answer = generate_answers(
            new_instance["predicted_type"]
            if use_predicted_type
            else new_instance["metadata"]["type"],
            [
                {
                    "generated": {"derivation": q},
                    "symmetric": True
                    if new_instance["metadata"]["relation"] in {"P47"}
                    else False,
                }
                for q in derivations
            ],
        )

    except Exception:
        return None

    new_instance["prediction"] = pred_answer

    if len(extra_dervs):

        derivations = extra_dervs[
            (
                new_instance["metadata"]["database_idx"],
                new_instance["metadata"]["question_idx"],
            )
        ]
    else:
        derivations = reduce(lambda a, b: a + b, map(itemgetter("actual"), instances))
    derivations = (
        reduce(
            lambda a, b: a + b,
            map(
                lambda derv: process_lists(derv, instance["metadata"]["type"]),
                map(maybe_split_qtype, derivations),
            ),
        )
        if len(derivations)
        else []
    )

    derivations = list(derivations)

    try:
        actual_answer = generate_answers(
            new_instance["metadata"]["type"],
            [
                {
                    "generated": {"derivation": q},
                    "symmetric": True
                    if new_instance["metadata"]["relation"] in {"P47"}
                    else False,
                }
                for q in derivations
            ],
        )

        new_instance["actual"] = actual_answer
        return new_instance
    except Exception:
        print("actual error")
        print(
            instance["metadata"]["database_idx"], instance["metadata"]["question_idx"]
        )
        print(derivations)
        # raise e
        return None


def retokenize(dervs):
    return [
        tokenizer.decode(tokenizer.encode(derv), skip_special_tokens=True).strip()
        for derv in dervs
    ]


if __name__ == "__main__":
    setup_logging()
    questions_answers = defaultdict(list)

    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    parser.add_argument("--actual_file", required=False)
    args = parser.parse_args()

    use_predicted_type = True

    file = args.in_file
    out_file = args.out_file

    with open(file) as f:
        for line in f:
            instance = json.loads(line)
            db_idx = instance["metadata"]["database_idx"]
            q_idx = instance["metadata"]["question_idx"]
            instance["predicted_type"] = extract_operator(instance["prediction"][0])
            questions_answers[(db_idx, q_idx)].append(instance)

    extra_dervs = {}

    if args.actual_file:
        tokenizer = AutoTokenizer.from_pretrained("t5-base")
        with open(args.actual_file) as f:
            for db_idx, line in enumerate(f):
                database = json.loads(line)
                for q_idx, query in enumerate(database["queries"]):
                    dervs = query["derivations"]
                    extra_dervs[(db_idx, q_idx)] = retokenize(dervs)

    num_instances = len(questions_answers)
    num_correct_type = 0
    running_f1 = 0
    scored = 0

    sq_err = 0
    sq_err_cnt = 0
    with open(out_file, "w+") as of:
        for instances in questions_answers.values():

            new_instance = post_process_instances(instances, use_predicted_type)
            if new_instance is not None:

                if new_instance["predicted_type"] == new_instance["metadata"]["type"]:
                    num_correct_type += 1

                if new_instance["metadata"]["type"] == "count":

                    sq_err += (
                        new_instance["actual"][0] - new_instance["prediction"][0]
                    ) ** 2
                    sq_err_cnt += 1

                local_1 = f1(new_instance["actual"], new_instance["prediction"])
                running_f1 += local_1

                # if local_1 < 1:
                #     print(new_instance['actual'], new_instance['prediction'])
                #     print(local_1)

                scored += 1

                of.write(json.dumps(new_instance) + "\n")

    print(f"Correct prediction type: \t\t{num_correct_type/num_instances}")
    print(f"Global F1 type: \t\t{running_f1/scored}")
    print(sq_err / sq_err_cnt)
