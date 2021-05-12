import json
import random
from argparse import ArgumentParser
from collections import defaultdict, Counter
from copy import copy
from json import JSONDecodeError

from tqdm import tqdm

from dataset_creation.generation.question_to_db import generate_answers
from wikidata_common.kelm import KELMMongo
from wikidata_common.wikidata import Wikidata


def get_numeric_value(s, r, fact):
    if 'numeric' in fact['parse'][2][1]:
        return fact['parse'][2][0]
    return None


def generate_positive_question(qid, qs, q_heights, height=None):
    q_type = qid.split("_")[0]

    if len(qs) == 0:
        return qid, q_heights[qid], None, None
    generated_question = random.choice([f[0][0] for f in qs])
    try:
        generated_answer = generate_answers("", q_type, [{

            "qid": qid,
            "generated": {
                "question": f[0][0],
                "derivation": f[0][1]
            },
            "symmetric": "P47" in qid
        } for f in qs])
    except Exception as e:
        raise e

    return qid, q_heights[qid], generated_question, generated_answer
    #print(qid, q_heights[qid], generated_question, generated_answer)

#
# def generate_negative_question(qid, qs, q_heights, max_height):
#     return generate_positive_question(qid,,q_heights, max_height)

def generate_negative_bool(hf, question_template, origianal_hyp):
    candidate_negatives_1 = []
    for f in hf.keys():
        if f[1] == origianal_hyp[1] and f[0] != origianal_hyp[0] and f[2] != origianal_hyp[2]:
            candidate_negatives_1.append(f)

    if len(candidate_negatives_1):
        hyp_to_make_negative = list(copy(origianal_hyp))
        hyp_to_make_negative[2] = random.choice(candidate_negatives_1)[2]
        hyp_to_make_negative = tuple(hyp_to_make_negative)

        s,r,o = hyp_to_make_negative

        subject_name = wiki.get_by_id_or_uri(hyp_to_make_negative[0])['english_name']
        if hyp_to_make_negative[2].startswith("Q"):
            object_name = wiki.get_by_id_or_uri(hyp_to_make_negative[2])['english_name']
            if object_name is None:
                return None
        else:
            object_name = hyp_to_make_negative[2]
            assert object_name != origianal_hyp[2]

        subj_in_q = f"_{s}" if "$s" in question_template[0] else ""
        obj_in_q = f"_{o}" if "$o" in question_template[0] else ""

        s_key = question_template[1].split("[SEP]")[0].strip() if "$" in question_template[1] else ""
        sort_key = (f"_{s_key}" if "$" in question_template[1] else "") if r != "P47" else "_$both"

        qid = f"bool_{r}{subj_in_q}{obj_in_q}{sort_key}_art_false"
        out = [q.replace("$s", subject_name).replace("$o", object_name) for q in question_template]
        out[1] = "FALSE"

        return qid, "bool", out, hf[origianal_hyp]
    return None

def generate_joins_filter(hf, facts, qid, question_template, s, r, o, is_subject):
    subj_in_q = f"_{s}" if "$s" in question_template[0] else ""
    obj_in_q = f"_{o}" if "$o" in question_template[0] else ""

    source_mutations = additional_subjects if is_subject else additional_objects
    subj_or_obj_in_question = (subj_in_q and is_subject) or (obj_in_q and not is_subject)

    if subj_or_obj_in_question and r in source_mutations:
        candidate_additional = [(s, a) for a in source_mutations[r].keys()]

        subj_rels = {(h[0], h[1]) for h in hf.keys()}
        for additional_subj, additional_rel in filter(lambda s_a: s_a in subj_rels, candidate_additional):
            found_sros = [k for k in hf.keys() if k[0] == additional_subj and k[1] == additional_rel]
            found_sro = random.choice(found_sros)


            if found_sro[2].startswith("Q"):
                additional_object_name = wiki.get_by_id_or_uri(found_sro[2])['english_name']
            else:
                additional_object_name = found_sro[2]

            modifier = random.choice(source_mutations[r][additional_rel])
            modifier = modifier.replace("$AO", additional_object_name)

            subject_name = wiki.get_by_id_or_uri(s)["english_name"]
            object_name = wiki.get_by_id_or_uri(o)["english_name"] if o.startswith("Q") else o
            extended_question = [q.replace("$s", modifier if is_subject else subject_name).replace("$o", modifier if not is_subject else object_name) for q in question_template]

            hyps = set(hf[found_sro]).union(hf[(s,r,o)])

            # print("\n".join(facts[fact]['fact'] for fact in hyps))
            # print(extended_question[0])
            # print()
            yield (
                f"{qid}_join_{additional_rel}_{found_sro[2]}_{'subj' if is_subject else 'obj'}",
                qid.split("_")[0],
                extended_question,
                hyps
            )


def generate_joins_extra(hf, facts, qid, question_template, s, r, o, is_subject):
    source_mutations = extra_subjects if is_subject else extra_objects

    if r in source_mutations and ("argmin" in qid or "argmax" in qid) and question_template[1].startswith("$s"):
        candidate_additional = [(s, a) for a in source_mutations[r].keys()]

        subj_rels = {(h[0], h[1]) for h in hf.keys()}
        for additional_subj, additional_rel in filter(lambda s_a: s_a in subj_rels, candidate_additional):
            found_sros = [k for k in hf.keys() if k[0] == additional_subj and k[1] == additional_rel]

            additional_subj_name = " [LIST] ".join(
                (wiki.get_by_id_or_uri(sro[2])['english_name']) if sro[2].startswith("Q") else sro[2] for sro in
                found_sros)
            modifier = random.choice(source_mutations[r][additional_rel])

            subject_name = wiki.get_by_id_or_uri(s)['english_name']
            object_name = wiki.get_by_id_or_uri(o)['english_name'] if o.startswith("Q") else o

            stripped_template = question_template[0]\
                .replace("Which", "$XXT")\
                .replace("What is the", "$XXT")\
                .replace("Who is", "$XXT")\
                .replace("Who has", "$XXT")

            if "$XXT" not in stripped_template:
                print("Unable to template ", question_template[0])
                return None

            if "$X" in modifier:
                newq = modifier.replace("$X", stripped_template.replace("$XXT", "").replace("?", ""))
            else:
                newq = stripped_template.replace("$XXT", modifier)

            extended_question = (
                newq,
                question_template[1].replace("$s", subject_name).replace("$o", object_name) + " [SEP] " + additional_subj_name
            )

            hyps = set()
            hyps.update(hf[(s,r,o)])
            for h in found_sros:
                hyps.update(hf[h])

            #
            # print("\n".join(facts[fact]['fact'] for fact in hyps))
            # print(extended_question[0])
            # print(extended_question[1])
            # print()
            yield (
                f"{qid}_join_extra_{additional_rel}_{'subj' if is_subject else 'obj'}",
                qid.split("_")[0],
                extended_question,
                hyps
            )

def generate_joins(hf, facts, qid, question_template, s, r, o):
    yield from generate_joins_filter(hf, facts, qid, question_template, s, r, o, is_subject=True)
    yield from generate_joins_filter(hf, facts, qid, question_template, s, r, o, is_subject=False)
    yield from generate_joins_extra(hf, facts, qid, question_template, s, r, o, is_subject=True)
    yield from generate_joins_extra(hf, facts, qid, question_template, s, r, o, is_subject=False)




def map_triples_to_facts(facts):
    # Iterate through the facts and extract the hypotheses from each fact
    # Store the facts in a dictionary from [s,r,o] triple to the index of the fact
    hypotheses_facts = defaultdict(list)
    for idx, fact in enumerate(facts):
        for hyp in fact['valid_hypotheses']:
            # If the object is "numeric" (old version, replace it with the actual value)
            if hyp[2] == "numeric":
                hyp[2] = get_numeric_value(hyp[0], hyp[1], fact)
                if hyp[2] is None:
                    break

            hyp = tuple(hyp)
            hypotheses_facts[hyp].append(idx)

    return hypotheses_facts


def generate_derivations(hypotheses_facts, facts):
    derivations = []

    # For each S,R,O triple in the DB,generate a question_answer derivation from it
    for hyp in tqdm(hypotheses_facts.keys()):
        s, r, o = hyp

        # If not it's a relation that we have templates for skip it
        if r not in final_templates:
            continue

        # Get the canonical subject/object name
        subject_name = wiki.get_by_id_or_uri(s)['english_name']
        object_name = o if not o.startswith("Q") else wiki.get_by_id_or_uri(o)['english_name']

        question_types = set(final_templates[r].keys()).difference({'fact', '_subject', '_object'})

        # For all quesiton types (bool, set, min, max etc)
        for q_type in question_types:
            # Sample a question template
            question = random.choice(final_templates[r][q_type])

            # Swap the subject_name and object_name into the template
            out = [q.replace("$s", subject_name).replace("$o", object_name) for q in question]

            # Make the question ID
            subj_in_q = f"_{s}" if "$s" in question[0] else ""
            obj_in_q = f"_{o}" if "$o" in question[0] else ""
            s_key = question[1].split("[SEP]")[0].strip() if "$" in question[1] else ""
            sort_key = (f"_{s_key}" if "$" in question[1] else "") if r != "P47" else "_$both"
            qid = f"{q_type}_{r}{subj_in_q}{obj_in_q}{sort_key}"

            # Add this to the derivations
            derivations.append((
                qid,
                q_type,
                out,
                hypotheses_facts[hyp]
            ))

            gj = list(generate_joins(hypotheses_facts, facts, qid, question, s, r, o))
            derivations.extend(gj)

            # If the question is boolean generate a negatively sampled false one for it
            if q_type == "bool":
                generated = generate_negative_bool(hypotheses_facts, question, hyp)
                if generated is not None:
                    derivations.append(generated)

    return derivations


def build_questions_for_db(database):

    # Get the facts
    facts = database["metadata"]["raw"]
    hypotheses_facts = map_triples_to_facts(facts)

    # Generate all derivations for these facts
    derivations = generate_derivations(hypotheses_facts, facts)

    # For each fact/derivation build a lookup table for it's height and q/a
    by_qid = defaultdict(list)
    q_heights = defaultdict(list)
    for q in derivations:
        by_qid[q[0]].append((q[2], q[3]))
        q_heights[q[0]].append(q[3])


    final_questions = []
    # For each question in the derivations, generate it's positive answer
    for qid, qs in by_qid.items():
        try:
            _, qh, generated_question, generated_answer = generate_positive_question(qid, qs, q_heights)
        except TypeError:
            continue

        # Get the participating IDs of the facts in this Q/A
        ids = set()
        qh1_filtered = []
        for facts_for_q in qh:
            local_f = []
            for fact_in_triple in facts_for_q:
                ids.add(fact_in_triple)
                local_f.append(fact_in_triple)

            if len(local_f):
                qh1_filtered.append(local_f)


        # Either set the context to be the size of the DB

        question_height = len(facts) if random.randint(0,1) else random.choice(list(range(max(ids),len(facts))))
        assert len(qh1_filtered) == len(qs)
        final_questions.append((
            qid,
            generated_question,
            generated_answer,
            [q[0][1] for q in qs],
            qh1_filtered,
            ids,
            question_height
        ))


        # If question is a lookup then sampling between min(ids) and max(ids) should
        # change the generated answer. Sampling below min(ids) would return no answer
        if len(qs) > 1:
            sample_choices = list(range(min(ids) if min(ids) != max(ids) else 0, max(ids)))
            if not len(sample_choices):
                continue
            max_height = random.choice(sample_choices)
        else:
            max_height = random.choice(list(range(0, min(ids) + 1)))

        # Make a negative question (with a null answer)
        qs_negative = [q for q in qs if all(subfact < max_height for subfact in q[1])]

        try:
            _, qh2, _, negative_generated_answer = generate_positive_question(qid, qs_negative, q_heights, max_height)
        except TypeError:
            continue
        # print(generated_question, negative_generated_answer, max_height)


        qh2_filtered = []
        new_ids = set()
        for facts_for_q in qh2:
            local_f = []
            for fact_in_triple in facts_for_q:
                if fact_in_triple < max_height:
                    new_ids.add(fact_in_triple)
                local_f.append(fact_in_triple)

            if len(local_f) and all(f < max_height for f in local_f):
                qh2_filtered.append(local_f)

        assert len(qh2_filtered) == len(qs_negative), (qh2_filtered, qs_negative)

        final_questions.append((
            qid,
            generated_question,
            negative_generated_answer,
            [q[0][1] for q in qs_negative],
            qh2_filtered,
            new_ids,
            max_height
        ))

        # TODO If question is a join then sampling between a joined fact should generate zero output

    # json.dumps({"metadata": {"raw": sampled}, "facts": [f['fact'] for f in sampled]})

    return final_questions


def group_derivations(ids_grouped, derivations):
    all_unique = defaultdict(list)

    for grp, derv in zip(ids_grouped, derivations):
        all_unique[tuple(grp)].append(derv)

    all_zipped = [(k," [LIST] ".join(v)) for k,v in all_unique.items()]
    return list(zip(*all_zipped)) if len(all_zipped) else ([],[])

if __name__ == "__main__":
    wiki = Wikidata()
    kelm = KELMMongo()

    with open("generate_v1.5.json") as f:
        final_templates = json.load(f)

    with open("filter_subjects.json") as f:
        additional_subjects = json.load(f)

    with open("filter_objects.json") as f:
        additional_objects = json.load(f)

    with open("expand_objects.json") as f:
        extra_objects = json.load(f)

    with open("expand_subject.json") as f:
        extra_subjects = json.load(f)

    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    args = parser.parse_args()

    stats_qtype = defaultdict(int)
    stats_num_facts = defaultdict(int)
    stats_rel = defaultdict(int)
    stats_height = defaultdict(int)
    stats_answer = Counter()
    with open(args.in_file) as f, open(args.out_file,"w+") as of:
        for line in f:
            # Load the DB as json line
            try:
                database = json.loads(line)
            except JSONDecodeError as e:
                continue

            random.shuffle(database["metadata"]["raw"])
            database["facts"] = [fact["fact"] for fact in database["metadata"]["raw"]]
            database["queries"] = []
            db_questions = build_questions_for_db(database)

            for q in db_questions:
                (
                    qid,
                    generated_question,
                    answer,
                    derivations,
                    ids_grouped,
                    ids_flat,
                    max_height
                ) = q


                qbits = qid.split("_",maxsplit=2)

                facts_grouped, derivations_grouped = group_derivations(ids_grouped,derivations)
                question = {
                    "id": qid,
                    "query": generated_question,
                    "answer": answer if answer is not None else [],
                    "derivations": derivations_grouped,
                    "facts": facts_grouped,
                    "height": max_height,
                    "relation": qbits[1],
                    "type": qbits[0]
                }
                database["queries"].append(question)
                if len(qbits) != 3:
                    print(qbits)
                else:
                    qtype, rel, _ = qbits
                    stats_qtype[qtype] +=1
                    stats_rel[rel] += 1
                    stats_height[max_height] += 1
                    stats_num_facts[len(ids_flat)] += 1
                    if answer is not None:
                        for a in answer:
                            stats_answer[a] += 1
                    else:
                        stats_answer[None] += 1
            random.shuffle(database["queries"])
            of.write(json.dumps(database)+"\n")

        print(json.dumps(stats_rel))
        print(json.dumps(stats_height))
        print(json.dumps(stats_num_facts))
        print(json.dumps(stats_qtype))
        print(json.dumps(stats_answer.most_common(50)))
