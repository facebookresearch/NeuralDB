import json
import logging
import random
from argparse import ArgumentParser
from collections import defaultdict, Counter
from functools import reduce

import numpy as np

from dataset_creation.generation.question_to_db import generate_answers
from log_helper import setup_logging

logger = logging.getLogger()

def generate_facts_for_db(db):
    generated = {}
    generated["question_answers"] = []
    generated["question_derivations"] = []
    generated["question_facts"] = []
    generated["question_types"] = []
    generated["questions"] = []
    generated["heights"] = []
    generated["rels"] = []


    disposable = list()
    bonus_count = 0
    bonus_facts = dict()
    by_db_idx = dict()
    for f in db:
        if "facts" not in f["instance"]:
            disposable.append(f)
        else:
            bonus_count += 1

    if bonus_count > 0:
        to_delete = random.sample(disposable,k=min(bonus_count, len(disposable)))
        for d in to_delete:
            db.remove(d)

    if get_q_size(db) > args.size:
        to_delete = random.sample(db, k=(get_q_size(db) - args.size)//2)
        for d in to_delete:
            db.remove(d)

    for f in db:
        if "facts" not in f["instance"]:
            pass
        else:
            bonus_count += 1
            bonus_facts["bonus_" + str(f["idx"])] = f["instance"]["facts"][1]
            by_db_idx["bonus_" + str(f["idx"])] = f

    for d in db:
        bonus_facts[d["idx"]] = d["instance"]['fact']
        by_db_idx[d['idx']] = d


    generated["indexes"] = set(f["idx"] for f in db)
    generated["qids"] = set(f["qid"] for f in db)
    generated["subjects"] = set(f["entity_ids"]["subject"] for f in db)
    generated["relations"] = set(f["entity_ids"]["relation"] for f in db)
    generated["subj_rels"] = set((f["entity_ids"]["subject"], f["entity_ids"]["relation"]) for f in db)


    # Store the list of questions we are gonna make queries over
    logger.info("Add positive facts (with original questions)")

    # Store the list of questions we are gonna make queries over
    logger.info("Add positive facts (with original questions)")
    active_questions = defaultdict(list)
    for query in db:
        active_questions[query["qid"]].append(query)


    # Make an ordering of the facts that the instances will be inserted in
    logger.info("Generate random order DB")

    ordering = list(bonus_facts.keys())
    random.shuffle(ordering)

    #random.shuffle(db)

    base_facts = []
    related = []

    qids = set()
    logger.info("Collect indexes")
    for idx in generated["indexes"]:
        questions = by_idx[idx]
        qids.update(questions)

    related= defaultdict(list)
    for q in qids:
        related[q].extend(a for a in by_question[q] if a['idx'] in generated['indexes'])

    fact_ids = []
    answers = []
    derivations = []
    heights = []
    types = []
    questions = []
    rels = []


    logger.info("Ordering")
    for i in range(len(ordering)):

        logger.info(f"Build {i}")
        height = len(ordering) - i

        active_facts_ids = ordering[:height]
        collected_indexes = set(active_facts_ids)

        for qid in qids:

            if height < len(ordering):
                if random.uniform(0,1) < 0.9:
                    continue

            if qid.startswith("set") or qid.startswith("count"):
                if random.uniform(0,1) < 0.45:
                    continue
            elif qid.startswith("bool") :

                if random.uniform(0,1) < 0.75:
                    continue


            filtered_facts = [a for a in related[qid] if a['idx'] in collected_indexes]

            if len(filtered_facts) == 0 and qid.startswith('bool'):
                if random.uniform(0,1) < 0.6:
                    continue
            elif len(filtered_facts) <= 1:# and not
                if random.uniform(0,1) < 0.7:
                    continue



            facts = by_question[qid]
            question_text = random.choice([a["generated"]["question"] for a in related[qid]])
            question_type = facts[0]["template"]["question_type"]

            def maybe_group(fact):
                ret = [ordering.index(fact["idx"])]
                if f"bonus_{fact['idx']}" in active_facts_ids:
                    ret += [ordering.index(f"bonus_{fact['idx']}")]
                return ret

            if "complex" in qid:
                newf = list(filter(lambda f:"bonus_"+str(f["idx"]) in active_facts_ids, filtered_facts))

                answers.append(generate_answers(question_text, question_type, newf))
                derivations.append([fact["generated"]["derivation"] if "bonus_"+str(fact["idx"]) in active_facts_ids else None for fact in filtered_facts])
                fact_ids.append([maybe_group(fact) for fact in filtered_facts])

                types.append(question_type+"_complex_"+("ok" if None not in answers[-1] and 0 not in answers[-1] and len(answers[-1]) else "none"))
            else:
                types.append(question_type)
                answers.append(generate_answers(question_text, question_type, filtered_facts))
                derivations.append([fact["generated"]["derivation"] for fact in filtered_facts])
                fact_ids.append([[ordering.index(fact["idx"])] for fact in filtered_facts])

            heights.append(height)
            questions.append(question_text)
            rels.append([fact["entity_ids"]["relation"] for fact in filtered_facts])


    master_answers = set() #linearize(a) for a in zip(generated["questions"], generated["question_answers"]))
    generate_counts = Counter()

    generated["qs"] = []
    for question, answer, qtype, fact, derivation, height, rel in zip(questions, answers, types, fact_ids, derivations, heights, rels):

        if qtype in {"set","count"}:

            if generate_counts[question] >= 4:
                continue
            elif generate_counts[question] >= 1 and generate_counts[linearize((question,answer))] <= 2:
                if random.uniform(0,1) < 0.8:
                    continue
            elif generate_counts[question] >= 1:
                continue

            if "complex" not in qtype and "none" not in qtype and random.uniform(0, 1) > 0.5:
                continue

        elif qtype in {"min","max","argmin","argmax"}:
            if generate_counts[question] >= 4:
                continue
            elif generate_counts[question] >= 1 and generate_counts[linearize((question,derivation))] <= 2:
                if random.uniform(0,1) < 0.8:
                    continue
            elif generate_counts[question] >= 1:
                continue

        elif qtype in {"bool"}:
            if generate_counts[question] >= 2:
                continue
            elif generate_counts[question] >= 1 and generate_counts[linearize((question, answer))] == 0:
                if random.uniform(0, 1) < 0.3:
                    continue

            if "complex" not in qtype and "none" not in qtype and random.uniform(0, 1) > 0.5:
                continue

        generate_counts[question] += 1
        generate_counts[linearize((question, answer))] += 1

        # For all DB of facts, then create the questions and answers associated with that question
        generated["qs"].append({
            "question": question.strip().replace("Whow many","How many"),
            "answer": answer,
            "type": qtype,
            "facts": fact,
            "deriations": derivation,
            "height": height,
            "relation": rel,
            "ids": [by_db_idx[ordering[f[0]]]['entity_ids'] for f in fact],
        })

    random.shuffle(generated["qs"])
    generated["facts"] =[]
    generated["facts"] = [bonus_facts[q] for q in ordering]
    logger.info(f"Added {len(generated['qs'])} queries to DB")
    return generated


def generate_db_facts(dbs):
    for db in dbs:
        try:
            generated = generate_facts_for_db(db)
            yield generated
        except Exception as e:
            logger.error(e)


def read_questions_into_dict(questions_file):
    questions = defaultdict(list)
    with open(questions_file) as f:
        for idx,line in enumerate(f):
            instance = json.loads(line)
            questions[instance["qid"]].append(instance)
    return questions

def partition_questions(by_question, short=5, long=10):
    by_len = defaultdict(list)
    for k, v in by_question.items():
        by_len[len(v)].append(k)

    long_questions = []
    medium_questions = []
    short_questions = []
    singleton_questions = []

    for i in by_len.keys():
        if i == 1:
            singleton_questions.extend(by_len[i])
        elif i >= 2 and i < short:
            short_questions.extend(by_len[i])
        elif i >= short and i < long:
            medium_questions.extend(by_len[i])
        elif i >= long:
            long_questions.extend(by_len[i])

    return singleton_questions, short_questions, medium_questions, long_questions

def partition_subject_relation(by_question):
    by_sub_rel = defaultdict(list)
    for k, v in by_question.items():
        for q in v:
            subj, rel = q["entity_ids"]["subject"],q["entity_ids"]["relation"]
            by_sub_rel[(subj,rel)].append(k)

    return by_sub_rel

def partition_subject(by_question):
    by_sub_rel = defaultdict(list)
    for k, v in by_question.items():
        for q in v:
            subj, rel = q["entity_ids"]["subject"],q["entity_ids"]["relation"]
            by_sub_rel[subj].append(k)

    return by_sub_rel

def partition_relation(by_question):
    by_sub_rel = defaultdict(list)
    for k, v in by_question.items():
        for q in v:
            subj, rel = q["entity_ids"]["subject"],q["entity_ids"]["relation"]
            by_sub_rel[rel].append(k)

    return by_sub_rel

def partition_idx(by_question):
    by_idx = defaultdict(list)
    for k, v in by_question.items():
        for q in v:
            idx = q["idx"]
            by_idx[idx].append(k)

    return by_idx

def linearize(pos):
    return (pos[0],tuple(pos[1]))


def get_q_size(questions):
    return sum([1 if "facts" not in instance["instance"] else len(instance["instance"]["facts"]) for instance in questions])


def sample_databases(num_to_generate, db_target_size, partitioned_questions, by_question,skip_entities):
    num_generated = 0
    while num_generated < num_to_generate:
        num_generated += 1
        db = []


        complex_questions = list(filter(lambda k: "complex" in k, by_question.keys()))

        for q in random.sample(complex_questions, k=3):
            db.extend(random.sample(by_question[q],
                                min(10, min(db_target_size - len(db), len(by_question[q])))))


        # Iterate through questions and make DBs containing facts only
        while len(db) < db_target_size:
            current_indexes = set(f["idx"] for f in db)



            # First pick whether we are adding a singleton, short, medium or long query
            question_set = random.choices(partitioned_questions, weights=sample_probs)[0]


            if len(question_set):
                # Pick a question from that set and add all facts to the DB
                sampled_question = random.choice(question_set)

                sampled_facts = random.sample(by_question[sampled_question],min(25, min(db_target_size - len(db), len(by_question[sampled_question]))))


                # Don't add duplicate facts
                db.extend(filter(lambda f: f["idx"] not in current_indexes and f['entity_ids']['subject'] not in skip_entities and f['entity_ids']['object'] not in skip_entities, sampled_facts))

        logger.info("Constructed DB of size {} queries".format(len(db)))
        yield db


if __name__ == "__main__":
    setup_logging()

    parser = ArgumentParser()
    parser.add_argument("questions_file")
    parser.add_argument("out_file")
    parser.add_argument("--size",help="Target size of facts in DB", type=int, default=50)
    parser.add_argument("--extra_negative_facts",help="Extra negative facts to add to DB", type=int, default=10)
    parser.add_argument("--num_to_make", help="Target size of facts in DB", type=int, default=5)
    parser.add_argument("--num_to_make_test", help="Target size of facts in DB", type=int, default=5)
    parser.add_argument("--short", help="Questions over <N of these facts (but >2) will be labeled as short questions.", type=int, default=5)
    parser.add_argument("--long", help="Questions>M (but <M) with be labeled as long questions", type=int, default=10)
    parser.add_argument("--weights", help="Sample weights for size of queries (short, medium, long). "
                                          "The rest is padded with singletons", type=float, nargs=3, default=[0.3,0.1,0.1])

    args = parser.parse_args()
    logger.info(repr(args))

    db_target_size = args.size
    num_dbs_to_make = args.num_to_make
    num_dbs_to_make_test = args.num_to_make_test

    # First set the sample weights and make sure that they add up to 1
    singleton_prob = 1-np.sum(args.weights)
    sample_probs = [singleton_prob] + args.weights
    assert singleton_prob >= 0
    logger.info("Sample probabilities: {} ".format(str(sample_probs)))

    # Read the questions in the dataset into a dictionary
    by_question = read_questions_into_dict(args.questions_file)
    by_subj_rel = partition_subject_relation(by_question)
    by_subj = partition_subject(by_question)
    by_rel = partition_relation(by_question)
    by_idx = partition_idx(by_question)
    all_questions = list(by_question.keys())

    logger.info(f"Num questions: {len(by_question)}")
    logger.info(f"Num sub.rel pairs: {len(by_subj_rel)}")
    logger.info(f"Num subjects: {len(by_subj)}")
    logger.info(f"Num relations: {len(by_rel)}")

    # Partition them in to singleton/small/medium/long
    partitioned_questions = partition_questions(by_question)

    stats_type = Counter()
    stats_lens = Counter()
    stats_heights = Counter()

    skip_subjects = set()
    with open(f"{args.out_file}_train","w+") as of:
        for db in generate_db_facts(
                sample_databases(num_dbs_to_make, db_target_size-args.extra_negative_facts, partitioned_questions, by_question, set())):

            for q in db["qs"]:
                stats_type[q["type"]] += 1
                stats_lens[len(q["facts"])] += 1

                stats_heights[q['height']] += 1

            ret_obj = {"facts": db["facts"], "queries":db["qs"]}
            skip_subjects.update(reduce(lambda a, b: a + b, [[e['subject'] for e in d['ids']] + [e['object'] for e in d['ids']] for d in db['qs']]))
            of.write(json.dumps(ret_obj)+"\n")

    ss2 = set()
    with open(f"{args.out_file}_dev","w+") as of:
        for db in generate_db_facts(
                sample_databases(num_dbs_to_make_test, db_target_size-args.extra_negative_facts, partitioned_questions, by_question, skip_subjects)):

            for q in db["qs"]:
                stats_type[q["type"]] += 1
                stats_lens[len(q["facts"])] += 1

                stats_heights[q['height']] += 1

            ret_obj = {"facts": db["facts"], "queries":db["qs"]}
            ss2.update(reduce(lambda a, b: a + b, [[e['subject'] for e in d['ids']] + [e['object'] for e in d['ids']] for d in db['qs']]))
            of.write(json.dumps(ret_obj)+"\n")

    ss3 = set()
    skip_subjects.update(ss2)
    with open(f"{args.out_file}_test","w+") as of:
        for db in generate_db_facts(
                sample_databases(num_dbs_to_make_test, db_target_size-args.extra_negative_facts, partitioned_questions, by_question, skip_subjects)):

            for q in db["qs"]:
                stats_type[q["type"]] += 1
                stats_lens[len(q["facts"])] += 1
                stats_heights[q['height']] += 1

            ret_obj = {"facts": db["facts"], "queries":db["qs"]}
            ss3.update(reduce(lambda a, b: a + b, [[e['subject'] for e in d['ids']] + [e['object'] for e in d['ids']] for d in db['qs']]))
            of.write(json.dumps(ret_obj)+"\n")

    print(stats_type)
    print(stats_lens)
    print(stats_heights)
