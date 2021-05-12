import itertools
import json
import random
from collections import Counter
from copy import copy

import numpy as np
from nltk import word_tokenize
from nltk import ngrams
from argparse import ArgumentParser

from similarity.levenshtein import Levenshtein
from similarity.normalized_levenshtein import NormalizedLevenshtein
from tqdm import tqdm
from nltk.tokenize.treebank import TreebankWordDetokenizer
from wikidata_common.wikidata import Wikidata

def convert_numeric_hypothesis(parses, hypotheses):
    for hypothesis in hypotheses:
        s,r,o = hypothesis

        if s == "numeric":
            hypothesis[0] = f"numeric{parses[0][0]}"

        if o == "numeric":
            hypothesis[2] = f"numeric{parses[2][0]}"

    return hypotheses

def generate_hypotheses(filename):
    with open(filename) as f:
        for idx, line in tqdm(enumerate(f),total=14300808):
            instance = json.loads(line)
            instance["idx"] = idx
            try:
                yield from zip(instance["valid_hypotheses"], itertools.repeat(instance, len(instance["valid_hypotheses"])))
            except Exception as e:
                pass


def normalize_subject(subject_name,fact):
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
        fact = TreebankWordDetokenizer().detokenize(fact.split()).replace(" 's", "'s").replace(
            " ,", ",")

        if subject_name not in fact:
            return None

        assert subject_name in fact, f"Subject {subject_name} was not in {fact}"
    return fact

def from_dict(object_dict):
    out_str = ""
    if "year" in object_dict:
        out_str += object_dict.pop('year')

        if "month" in object_dict:
            out_str += '-'
            out_str += object_dict.pop('month')

            if "day" in object_dict:
                out_str += '-'
                out_str += object_dict.pop('day')

    if len(object_dict):
        print(object_dict.keys())
        raise Exception()
    return out_str

if __name__ == "__main__":
    # templates = {
    #     "P54": {
    #         "bool": [["Does $S $P $O?", ["play for"]],
    #                  ["Is $S $P $O?", ["a player for", "a member of", "part of the team of", "a player at"]],
    #                  ["Does $O $P $S?", "'s membership include", "'s players include"]],
    #         "argmin_$O": [["Which $P has the $P players?",
    #                        ["sports team", "club", "team"],
    #                        ["fewest", "least", "lowest number of"]],
    #                       ["What is the $P $P?",
    #                        ["smallest"],
    #                        ["sports team", "sports club", "team"]],
    #                       ["What is the $P with the $P $P?",
    #                        ["sports team", "sports club", "team"],
    #                        ["fewest", "lowest number of", "least"],
    #                        ["players", "members"]
    #                        ]],
    #         "argmin_$S": [["Who has $P for the $P $P?",
    #                        ["been a player for", "been a member of", "played for"],
    #                        ["the fewest", "the least number of", "the lowest number of", "the least"],
    #                        ["teams", "sports teams", "sports clubs", "clubs"]],
    #                       ["What is the $P $P?", ["smallest"],
    #                        ["sports team", "sports club", "team"]
    #                        ]]
    #
    #     }
    # }
    #



    wikidata = Wikidata()
    generated = []

    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    args = parser.parse_args()

    skip = {"is","a","of","between","on","in"}

    with open("generate_v1.5.json") as f:
        final_templates = json.load(f)

    hyps = generate_hypotheses(args.in_file)
    rel_cnt = Counter()
    idx = 0
    dropped_s = 0
    dropped_o = 0
    with open(args.out_file,"w+") as out_file:
        for (s,r,o),instance in hyps:

            idx+=1
            if "\u2047" in instance["candidate"]:
                continue

            fact = instance["candidate"]

            # Hack fix for P35
            if r=="P35":
                tmp = s
                s = o
                o = tmp

            relation = wikidata.get_by_id_or_uri(r)
            relation_name = relation["english_name"]

            subject = wikidata.get_by_id_or_uri(s)
            subject_name = subject["english_name"]

            if o.startswith("Q"):
                object = wikidata.get_by_id_or_uri(o)
                object_name = object["english_name"] if object is not None else None
            else:
                object_name = o.replace("+","")

            if object_name is None:
                continue

            fact = instance["candidate"].strip()
            fact = normalize_subject(subject_name, fact)
            if fact is None:
                dropped_s += 1
                continue

            if o.startswith("Q"):
                fact = normalize_subject(object_name, fact)
                if fact is None:
                    dropped_o +=1
                    continue

            if r not in final_templates or fact is None or object_name is None or subject_name is None:
                #print(f"Missing {r}")
                continue

            template = final_templates[r]
            available_question_types = list(set(template.keys()).difference({"fact", "_subject", "_object"}))

            for question_type in available_question_types:
                question = random.choice(template[question_type])

                if r == "P47":
                    if "[SEP]" in question[1]:
                        question[1] = question[1].replace("[SEP]", "[SYM]")
                        if question[1] == "$o [SYM] $s":
                            question[1] = "$s [SYM] $o"

                out = [q.replace("$s",subject_name).replace("$o",object_name) for q in question]
                out_type = question[1].split("[SEP]")[0].strip() if r!="P47" else "$both"

                subj_in_q = f"_{s}" if "$s" in question[0] else ""
                obj_in_q = f"_{o}" if "$o" in question[0] else ""

                s_key = question[1].split("[SEP]")[0].strip() if "$" in question[1] else ""
                sort_key = (f"_{s_key}" if "$" in question[1] else "") if r!= "P47" else "$both"

                # print(fact)
                # print(subject_name)
                # print(question[0].replace("$s", subject_name).replace("$o",
                #                                                                     object_name.replace("numeric+",
                #                                                                                         "").replace(
                #                                                                         "numeric-", "-")))

                qid = f"{question_type}_{r}{subj_in_q}{obj_in_q}{sort_key}"
                out_file.write(json.dumps({
                    "qid": qid,
                    "idx": instance["idx"],
                    "symmetric": r=="P47",
                    "template": {
                        "question": question[0],
                        "derivation": question[1],
                        "question_type": question_type
                    },
                    "entity_ids": {
                        "subject": s,
                        "object": o,
                        "relation": r
                    },
                    "entities": {
                        "subject": subject_name,
                        "object": object_name
                    },
                    "generated": {
                        "question": question[0].replace("$s", subject_name).replace("$o",
                                                                                    object_name.replace("numeric+",
                                                                                                        "").replace(
                                                                                        "numeric-", "-")),
                        "derivation": question[1].replace("$s", subject_name).replace("$o", object_name),
                        "fact": fact.replace("$s", subject_name).replace("$o",
                                                                         object_name.replace("numeric+", "").replace(
                                                                             "numeric-", "-")),
                    },
                    "instance": {
                        "reference": instance['reference'].strip(),
                        "candidate": instance["candidate"].strip(),
                        "fact": fact
                    },
                    "other_hyps": instance["valid_hypotheses"]

                }) + "\n")

                rel_cnt[r] += 1

            if idx % 100 == 0:
                print(f"{dropped_s} - {dropped_o}")
                print("\n",rel_cnt,"\n")
