import json
import random
from copy import copy

import itertools
import numpy as np
from argparse import ArgumentParser
from nltk import ngrams
from nltk import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from similarity.normalized_levenshtein import NormalizedLevenshtein
from tqdm import tqdm
from wikidata_common.wikidata import Wikidata


def convert_numeric_hypothesis(parse, hypotheses):
    for hypothesis in hypotheses:
        s, r, o = hypothesis

        if s == "numeric":
            hypothesis[0] = f"numeric{parse[0][0]}"

        if o == "numeric":
            hypothesis[2] = f"numeric{parse[2][0]}"

    return hypotheses


def generate_hypotheses(filename):
    with open(filename) as f:
        for idx, line in tqdm(enumerate(f), total=14300808):
            instance = json.loads(line)
            instance["idx"] = idx
            try:
                yield from zip(
                    convert_numeric_hypothesis(
                        instance["parse"], instance["valid_hypotheses"]
                    ),
                    itertools.repeat(instance, len(instance["valid_hypotheses"])),
                )
            except Exception:
                pass


if __name__ == "__main__":
    with open("generate_v1.5.json") as f:
        templates = json.load(f)

    wikidata = Wikidata()
    generated = []

    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    args = parser.parse_args()

    skip = {"is", "a", "of", "between", "on", "in"}
    hyps = generate_hypotheses(args.in_file)
    with open(args.out_file, "w+") as out_file:
        for (s, r, o), instance in hyps:
            if "\u2047" in instance["candidate"]:
                continue
            # try:
            if r in templates:
                template = templates[r]
                fact = random.choice(template["fact"])
                available_question_types = list(
                    set(template.keys()).difference({"fact", "_subject", "_object"})
                )

                for question_type in available_question_types:
                    question = random.choice(template[question_type])
                    instance["fact"] = copy(instance["candidate"]).strip()
                    # references = {}
                    # all_subjects, all_relations, all_objects = instance["parse"]
                    #
                    # references.update({id:all_subjects[0] for id in all_subjects[1]})
                    # references.update({id:all_objects[0] for id in all_objects[1]})
                    #
                    #
                    #
                    # subject_name = £references[s] # wikidata.get_by_id_or_uri(s)
                    # object_name = references[o] if o in references else o # wikidata.get_by_id_or_uri(o)

                    subject = wikidata.get_by_id_or_uri(s)
                    object = wikidata.get_by_id_or_uri(o)
                    subject_name = subject["english_name"]
                    object_name = object["english_name"] if object is not None else o
                    n = NormalizedLevenshtein()
                    mixed_case_subject = not subject_name.islower()
                    if mixed_case_subject and subject_name not in instance["fact"]:
                        toks = word_tokenize(instance["fact"])
                        all_grams = []
                        for i in range(1, len(toks)):
                            all_grams.extend(
                                " ".join(a) for a in ngrams(toks, i) if a[0] not in skip
                            )

                        scores = [
                            n.similarity(gram, subject_name) for gram in all_grams
                        ]
                        best_post = np.argmax(scores)
                        original_subject_name = all_grams[best_post]
                        if scores[best_post] < 0.5 or all_grams[best_post] == "name":
                            continue

                        instance["fact"] = " ".join(toks)
                        print(instance["fact"])
                        instance["fact"] = instance["fact"].replace(
                            original_subject_name, subject_name
                        )
                        print(instance["fact"])
                        print(
                            f"Replaced subject: {original_subject_name} with {subject_name}"
                        )
                        #
                        # print()

                        instance["fact"] = (
                            TreebankWordDetokenizer()
                            .detokenize(instance["fact"].split())
                            .replace(" 's", "'s")
                            .replace(" ,", ",")
                        )

                    mixed_case_object = not object_name.islower()
                    if (
                        mixed_case_object
                        and r != "P21"
                        and (object is not None and object_name not in instance["fact"])
                    ):
                        toks = word_tokenize(instance["fact"])
                        all_grams = []
                        for i in range(1, len(toks)):
                            all_grams.extend(
                                " ".join(a) for a in ngrams(toks, i) if a[0] not in skip
                            )

                        # n1 = [n.similarity(subject_name, " ".join(toks[:i])) for i in range(1,len(toks)+1)]
                        # end_pos = np.argmax(n1)+1
                        # n2 = [n.similarity(subject_name, " ".join(toks[i:end_pos])) for i in range(0, end_pos)]
                        # start_pos = np.argmax(n2)

                        # original_subject_name = TreebankWordDetokenizer().detokenize(toks[start_pos:end_pos])
                        scores = [n.similarity(gram, object_name) for gram in all_grams]
                        best_post = np.argmax(scores)

                        original_object_name = all_grams[best_post]
                        if scores[best_post] < 0.5 or all_grams[best_post] == "name":
                            continue

                        instance["fact"] = " ".join(toks)
                        # print(instance["fact"])
                        instance["fact"] = instance["fact"].replace(
                            original_object_name, object_name
                        )
                        # print(instance["fact"])
                        # print(f"Replaced object: {original_object_name} with {object_name}")
                        #
                        # print()
                        instance["fact"] = (
                            TreebankWordDetokenizer()
                            .detokenize(instance["fact"].split())
                            .replace(" 's", "'s")
                            .replace(" ,", ",")
                        )

                    if (
                        subject_name not in instance["fact"]
                        or object_name not in instance["fact"]
                    ):
                        continue

                    assert (
                        subject_name in instance["fact"]
                    ), f"Subject {subject_name} was not in {instance['fact']}"
                    assert (
                        object_name in instance["fact"] or object_name not in instance
                    ), f"Object {object_name} was not in {instance['fact']}"

                    subj_in_q = f"_{s}" if "$s" in question[0] else ""
                    obj_in_q = f"_{o}" if "$o" in question[0] else ""

                    s_key = (
                        question[1].split("[SEP]")[0].strip()
                        if "$" in question[1]
                        else ""
                    )
                    sort_key = f"_{s_key}" if "$" in question[1] else ""

                    qid = f"{question_type}_{r}{subj_in_q}{obj_in_q}{sort_key}"
                    out_file.write(
                        json.dumps(
                            {
                                "qid": qid,
                                "idx": instance["idx"],
                                "template": {
                                    "question": question[0],
                                    "derivation": question[1],
                                    "question_type": question_type,
                                },
                                "entity_ids": {
                                    "subject": s,
                                    "object": o,
                                    "relation": r,
                                },
                                "entities": {
                                    "subject": subject_name,
                                    "object": object_name,
                                },
                                "generated": {
                                    "question": question[0]
                                    .replace("$s", subject_name)
                                    .replace(
                                        "$o",
                                        object_name.replace("numeric+", "").replace(
                                            "numeric-", "-"
                                        ),
                                    ),
                                    "derivation": question[1]
                                    .replace("$s", subject_name)
                                    .replace("$o", object_name),
                                    "fact": fact.replace("$s", subject_name).replace(
                                        "$o",
                                        object_name.replace("numeric+", "").replace(
                                            "numeric-", "-"
                                        ),
                                    ),
                                },
                                "instance": {
                                    "reference": instance["reference"],
                                    "candidate": instance["candidate"],
                                    "fact": instance["fact"],
                                },
                            }
                        )
                        + "\n"
                    )
        # except Exception as e:
        #     print(e)
