import json
import random
from argparse import ArgumentParser
from copy import copy

from tqdm import tqdm

from dataset_creation.new.v2_question_generation import normalize_subject
from wikidata_common.kelm import KELMMongo
from wikidata_common.wikidata import Wikidata


additional_subjects = {
    "P54": {
        "P2067": ["someone who weighs $AO"],  # Weight
        "P2048": ["someone $AO tall"],  # Height
        "P21": ["someone who is a $AO"],  # Gender
        "P413": ["someone who plays $AO"],  # Play position
        "P569": ["someone born on $AO"],  # born
        "P27": ["someone from $AO"]  # Place of birth
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


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    args = parser.parse_args()

    kelm = KELMMongo()
    wikidata = Wikidata()

    fact_cache = dict()

    with open(args.in_file) as f, open(args.out_file,"w+") as outf:
        for line in tqdm(f,total=867383):
            instance = json.loads(line)

            question = instance["template"]["question"],instance["template"]["derivation"]
            question_type = instance["template"]["question_type"]

            s = instance["entity_ids"]["subject"]
            r = instance["entity_ids"]["relation"]
            o = instance["entity_ids"]["object"]

            object_name = instance["entities"]["object"]
            subject_name = instance["entities"]["subject"]

            subj_in_q = f"_{s}" if "$s" in question[0] else ""
            obj_in_q = f"_{o}" if "$o" in question[0] else ""
            qid = instance["qid"]
            additional = []

            s_key = question[1].split("[SEP]")[0].strip() if "$" in question[1] else ""
            sort_key = (f"_{s_key}" if "$" in question[1] else "") if r != "P47" else "$both"
            if subj_in_q:

                if r in additional_subjects:
                    extra = list(kelm.find_entity(s))
                    modifiers = []
                    for found in extra:
                        if any(asubj in found['relations'] for asubj in additional_subjects[r].keys()):
                            for valid_hy in filter(lambda hyp: hyp[0] == s and hyp[1] in additional_subjects[r],
                                                   found["valid_hypotheses"]):
                                if valid_hy in instance['other_hyps']:
                                    continue
                                sub_template = random.choice(additional_subjects[r][valid_hy[1]])
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
                                    modifiers.append((sub_template.replace("$AO", replacement),found,valid_hy[1],valid_hy[2], replacement))

                    for modifier,found,rel, match_subject_id,replacement in modifiers:
                        extra_generated = question[0].replace("$s", modifier).replace("$o", object_name)
                        additional.append({"question": extra_generated,
                                           "derivation":question[1].replace("$s",subject_name).replace("$o",object_name),
                                           "extra_fact":found,"extra_rel":rel,
                                           "replacement": replacement,
                                           "match": subject_name,
                                           "qid": f"{question_type}_{r}_{rel}_{replacement}_{o}{sort_key}_complex"})

            if obj_in_q and not isinstance(o, dict) and o.startswith("Q"):

                if r in additional_objects:
                    extra = list(kelm.find_entity(o))
                    modifiers = []
                    for found in extra:
                        if any(asubj in found['relations'] for asubj in additional_objects[r].keys()):
                            for valid_hy in filter(lambda hyp: hyp[0] == o and hyp[1] in additional_objects[r],
                                                   found["valid_hypotheses"]):
                                if valid_hy in instance['other_hyps']:
                                    continue

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
                                    modifiers.append((sub_template.replace("$AO", replacement),found,valid_hy[1],valid_hy[2], replacement))


                    for modifier,found,rel,match_object_id, replacement in modifiers:
                        extra_generated = question[0].replace("$s", subject_name).replace("$o", modifier)
                        additional.append({"question": extra_generated,
                                           "derivation":question[1].replace("$s",subject_name).replace("$o",object_name),
                                           "extra_fact":found,
                                           "extra_rel":rel,
                                           "replacement": replacement,
                                           "match":object_name,
                                           "qid": f"{question_type}_{r}_{s}_{rel}_{match_object_id}{sort_key}_complex"})

            if not subj_in_q and not obj_in_q and not isinstance(o, dict) and o.startswith("Q"):
                modifiers = []

                if r in expansions_subject:
                    if question[1].startswith("$o"):
                        extra = list(kelm.find_entity(o))
                        modifiers = []
                        for found in extra:

                            if any(asubj in found['relations'] for asubj in expansions_subject[r].keys()):
                                for valid_hy in filter(lambda hyp: hyp[0] == o and hyp[1] in expansions_subject[r],
                                                       found["valid_hypotheses"]):
                                    if valid_hy in instance['other_hyps']:
                                        continue

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
                                    modifiers.append((sub_template, replacement, found, valid_hy[1], object_name))

                if r in expansions_object:
                    if question[1].startswith("$s"):
                        extra = list(kelm.find_entity(s))
                        modifiers = []
                        for found in extra:
                            if any(asubj in found['relations'] for asubj in expansions_object[r].keys()):
                                for valid_hy in filter(lambda hyp: hyp[0] == s and hyp[1] in expansions_object[r],
                                                       found["valid_hypotheses"]):
                                    if valid_hy in instance['other_hyps']:
                                        continue
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
                                    modifiers.append((sub_template, replacement, found, valid_hy[1],subject_name))

                for modifier, eid, found, rel,match in modifiers:
                    xt = question[0].replace("Which", "$XXT").replace("What is the", "$XXT").replace("Who is",
                                                                                                     "$XXT").replace(
                        "Who has", "$XXT")

                    if "$XXT" not in xt:
                        print("Unable to template ", question[0])
                        break

                    if "$X" in modifier:
                        newq = modifier.replace("$X", xt.replace("$XXT", "").replace("?", ""))
                    else:
                        newq = xt.replace("$XXT", modifier)


                    additional.append({"question": newq,
                                       "derivation": question[1].replace("$s",subject_name).replace("$o",object_name) + " [SEP] " + eid,
                                       "extra_fact": found,
                                       "extra_rel": rel,
                                       "replacement": eid,
                                       "match": match,
                                       "qid": f"{qid}_extra_{rel}_complex"})


            outf.write(json.dumps(instance) +"\n")

            if not len(additional):
                continue
            for add in random.sample(additional,k=1):
                new_fact = add["extra_fact"]["candidate"].strip()

                if new_fact not in fact_cache:
                    old_fact = copy(new_fact)
                    new_fact = normalize_subject(add["match"], new_fact)
                    if new_fact is None:
                        continue

                    new_fact = normalize_subject(add["replacement"], new_fact)
                    if new_fact is None:
                        continue

                    fact_cache[old_fact] = new_fact

                else:
                    new_fact = fact_cache[new_fact]

                new_instance = copy(instance)
                new_instance["qid"] = add['qid']
                new_instance["generated"]["question"] = add["question"]
                new_instance["instance"]["facts"] = [instance["instance"]["fact"], new_fact]
                new_instance["generated"]["derivation"] = add["derivation"]

                outf.write(json.dumps(new_instance) + "\n")

