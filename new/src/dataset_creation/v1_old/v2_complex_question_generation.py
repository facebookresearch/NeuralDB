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

from wikidata_common.kelm import KELMMongo
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


    kelm = KELMMongo()
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

            if r not in final_templates or fact is None:
                #print(f"Missing {r}")
                continue

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

            if object_name is None or subject_name is None or fact is None:
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

                finalized = {"P54"}
                additional_subjects = {
                    "P54": {
                        "P2067": ["someone who weighs $AO"],    # Weight
                        "P2048": ["someone $AO tall"],          # Height
                        "P21": ["someone who is a $AO"],                 # Gender
                        "P413": ["someone who plays $AO"],                  # Play position
                        "P569": ["someone born on $AO"],        # born
                        "P27": ["someone from $AO"]             # Place of birth
                    },
                    "P50": {
                        "P136": ["a work with the genre $AO"],
                        "P495": ["a work originating from $AO"],
                        "P577": ["a work published on $AO"],
                    },
                    "P58": {
                        "P136": ["a work with the genre $AO"],
                        "P495": ["a work originating from $AO"],
                        "P577": ["a work published on $AO"],
                    },
                    "P69": {
                        "P27": ["someone from $AO"],
                        "P21": ["someone who is a $AO"],
                        "P108": ["someone who is employed by $AO"],
                        "P106": ["someone who works as a $AO"],
                        "P39": ["someone who is a $AO"],
                        "P166": ["someone who won a $AO"],
                        "P463": ["someone who is a member of $AO"],
                        "P937": ["someone who works in $AO"]
                    },

                }
                additional_objects = {
                    "P54": {
                        "P17": ["a club located in $AO", "a team located in $AO"],
                        "P118": ["a team in $AO"],
                    },
                    "P50": {

                        "P27": ["someone from $AO"],
                        "P21": ["someone who is a $AO"],
                        "P108": ["someone who is employed by $AO"],
                        "P106": ["someone who works as a $AO"],
                        "P39": ["someone who is a $AO"],
                        "P166": ["someone who won a $AO"],
                        "P463": ["someone who is a member of $AO"],
                        "P937": ["someone who works in $AO"]
                    },
                    "P58": {

                        "P27": ["someone from $AO"],
                        "P21": ["someone who is a $AO"],
                        "P108": ["someone who is employed by $AO"],
                        "P106": ["someone who works as a $AO"],
                        "P39": ["someone who is a $AO"],
                        "P166": ["someone who won a $AO"],
                        "P463": ["someone who is a member of $AO"],
                        "P937": ["someone who works in $AO"]
                    },
                    "P61": {
                        "P27": ["someone from $AO"],
                        "P21": ["someone who is a $AO"],
                        "P108": ["someone who is employed by $AO"],
                        "P106": ["someone who works as a $AO"],
                        "P39": ["someone who is a $AO"],
                        "P166": ["someone who won a $AO"],
                        "P463": ["someone who is a member of $AO"],
                        "P937": ["someone who works in $AO"]
                    },
                    "P69": {
                        "P17": ["an institution in $AO"],
                    },


                }

                expansions_subject = {
                    "P54": {
                        "P27": ["What is the citizenship of the player that"],
                        "P2067": ["What is the weight of the player that"],
                        "P2048": ["What is the height of the player that"],
                        "P569": ["What is the date of birth of the player that"],
                    },
                    "P50": {
                        "P136": ["What is the genre of the work of the"],
                        "P495": ["Where did the work that $X originate from?"],
                        "P577": ["When was the work that $X published"],
                    },
                    "P58": {
                        "P136": ["What is the genre of the work that"],
                        "P495": ["Where did the work that $X originate from?"],
                        "P577": ["When was the work that $X published"],
                    },
                    "P69": {
                        "P27": ["What is the country of the person that went to"],
                        "P21": ["What is the gender of the person that went to"],
                        "P108": ["What is the employer of the person that went to"],
                        "P106": ["What is the occupation of the person that went to"],
                        "P39": ["What is the position of the person that went to"],
                        "P166": ["What prize did the person that went to $X win?"],
                        "P463": ["What is the affiliation of the person that went to"],
                        "P937": ["What field does the person that went to $X work in?"]
                    },

                }

                expansions_object = {
                    "P54": {
                        "P17": ["What is the country of the player who"],
                        "P118": ["What is the league of the player who"],
                    },
                    "P50": {
                        "P27": ["What is the country of the person that"],
                        "P21": ["What is the gender of the person that"],
                        "P108": ["What is the employer of the person that"],
                        "P106": ["What is the occupation of the person that"],
                        "P39": ["What is the position of the person that"],
                        "P166": ["What prize did the person that $X win?"],
                        "P463": ["What is the affiliation of the person that"],
                        "P937": ["What is the field that $X works in?"]
                    },
                    "P61": {
                        "P27": ["What is the country of the person that"],
                        "P21": ["What is the gender of the person that"],
                        "P108": ["What is the employer of the person that"],
                        "P106": ["What is the occupation of the person that"],
                        "P39": ["What is the position of the person that"],
                        "P166": ["What prize did the person that $X win?"],
                        "P463": ["What is the affiliation of the person that"],
                        "P937": ["What is the field that $X works in?"]
                    },
                    "P69": {
                        "P27": ["What country is the institution of the person who has"],
                        "P463": ["What affiliation is the institution of the person that has"],
                        "P937": ["What is the field of the institution of the person that has"]
                    },

                }

                if subj_in_q:

                    print("NS",question_type)
                    if r in additional_subjects:
                        extra = list(kelm.find_entity(s))
                        modifiers = []
                        for found in extra:
                            if any(asubj in found['relations'] for asubj in additional_subjects[r].keys()):
                                for valid_hy in filter(lambda hyp: hyp[0] == s and hyp[1] in additional_subjects[r], found["valid_hypotheses"]):
                                    sub_template =  random.choice(additional_subjects[r][valid_hy[1]])
                                    if "$AO" in sub_template:
                                        if valid_hy[2].startswith("Q"):
                                            replacement = wikidata.get_by_id_or_uri(valid_hy[2])
                                            if replacement is not None:
                                                replacement = replacement['english_name']
                                                if replacement is None:
                                                    continue
                                            else:
                                                continue
                                        else:
                                            replacement = valid_hy[2]
                                        modifiers.append(sub_template.replace("$AO", replacement))



                        for modifier in modifiers:
                            extra_generated = question[0].replace("$s",modifier).replace("$o", object_name)
                            print("subject",extra_generated)

                if obj_in_q and not isinstance(o,dict) and o.startswith("Q"):

                    print("NO",question_type)
                    if r in additional_objects:
                        extra = list(kelm.find_entity(o))
                        modifiers = []
                        for found in extra:
                            if any(asubj in found['relations'] for asubj in additional_objects[r].keys()):
                                for valid_hy in filter(lambda hyp: hyp[0] == o and hyp[1] in additional_objects[r],
                                                       found["valid_hypotheses"]):
                                    sub_template = random.choice(additional_objects[r][valid_hy[1]])
                                    if "$AO" in sub_template:
                                        if valid_hy[2].startswith("Q"):
                                            replacement = wikidata.get_by_id_or_uri(valid_hy[2])
                                            if replacement is not None:
                                                replacement = replacement['english_name']
                                                if replacement is None:
                                                    continue
                                            else:
                                                continue
                                        else:
                                            replacement = valid_hy[2]
                                        modifiers.append(sub_template.replace("$AO", replacement))


                        for modifier in modifiers:

                            extra_generated = question[0].replace("$s", subject_name).replace("$o", modifier)
                            print("object",extra_generated)


                if not subj_in_q and not obj_in_q and not isinstance(o,dict) and o.startswith("Q"):
                    # Expand
                    print("NA",question_type, question[0])

                    modifiers = []

                    if r in expansions_subject:
                        if question[1].startswith("$o"):
                            extra = list(kelm.find_entity(o))
                            modifiers = []
                            for found in extra:
                                if any(asubj in found['relations'] for asubj in expansions_subject[r].keys()):
                                    for valid_hy in filter(lambda hyp: hyp[0] == o and hyp[1] in expansions_subject[r],
                                                           found["valid_hypotheses"]):
                                        sub_template = random.choice(expansions_subject[r][valid_hy[1]])

                                        if valid_hy[2].startswith("Q"):
                                            replacement = wikidata.get_by_id_or_uri(valid_hy[2])
                                            if replacement is not None:
                                                replacement = replacement['english_name']
                                                if replacement is None:
                                                    continue
                                            else:
                                                continue
                                        else:
                                            replacement = valid_hy[2]
                                        modifiers.append((sub_template, replacement))



                    if r in expansions_object:
                        if question[1].startswith("$s"):
                            extra = list(kelm.find_entity(s))
                            modifiers = []
                            for found in extra:
                                if any(asubj in found['relations'] for asubj in expansions_object[r].keys()):
                                    for valid_hy in filter(lambda hyp: hyp[0] == s and hyp[1] in expansions_object[r],
                                                           found["valid_hypotheses"]):
                                        sub_template = random.choice(expansions_object[r][valid_hy[1]])

                                        if valid_hy[2].startswith("Q"):
                                            replacement = wikidata.get_by_id_or_uri(valid_hy[2])
                                            if replacement is not None:
                                                replacement = replacement['english_name']
                                                if replacement is None:
                                                    continue
                                            else:
                                                continue
                                        else:
                                            replacement = valid_hy[2]
                                        modifiers.append((sub_template, replacement))


                    for modifier,eid  in modifiers:
                        xt = question[0].replace("Which","$XXT").replace("What is the", "$XXT").replace("Who is","$XXT").replace("Who has","$XXT")

                        if "$XXT" not in xt:
                            print("Unable to template ",question[0])
                            break


                        if "$X" in modifier:
                            newq = modifier.replace("$X",xt.replace("$XXT","").replace("?",""))
                        else:
                            newq = xt.replace("$XXT",modifier)

                        print("expand",r,subject_name,object_name, newq, question[1] + " [SEP] " + eid)


                    # Filter

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
                    }

                }) + "\n")

                rel_cnt[r] += 1

            if idx % 100 == 0:
                print(f"{dropped_s} - {dropped_o}")
                print("\n",rel_cnt,"\n")
