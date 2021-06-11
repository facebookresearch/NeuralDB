import json
import logging
import random
from collections import defaultdict, Counter

import numpy as np
from argparse import ArgumentParser

from ndb_data.util.log_helper import setup_logging

logger = logging.getLogger()


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
        int(item)
        return True
    except Exception:

        try:
            float(item)
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


def partition_questions(by_question, short=5, long=10):
    by_len = defaultdict(list)
    for k, v in by_question.items():
        by_len[len(v)].append(k)

    long_questions = []
    medium_questions = []
    short_questions = []
    singleton_questions = []

    for i in range(1, 100):
        if i == 1:
            singleton_questions.extend(by_len[i])
        elif i >= 2 and i < short:
            short_questions.extend(by_len[i])
        elif i >= short and i < long:
            medium_questions.extend(by_len[i])
        elif i >= long:
            long_questions.extend(by_len[i])
        print(i, len(by_len[i]))

    return singleton_questions, short_questions, medium_questions, long_questions


def partition_subject_relation(by_question):
    by_sub_rel = defaultdict(list)
    for k, v in by_question.items():
        for q in v:
            subj, rel = q["entity_ids"]["subject"], q["entity_ids"]["relation"]
            by_sub_rel[(subj, rel)].append(k)

    return by_sub_rel


def partition_subject(by_question):
    by_sub_rel = defaultdict(list)
    for k, v in by_question.items():
        for q in v:
            subj, _ = q["entity_ids"]["subject"], q["entity_ids"]["relation"]
            by_sub_rel[subj].append(k)

    return by_sub_rel


def partition_relation(by_question):
    by_sub_rel = defaultdict(list)
    for k, v in by_question.items():
        for q in v:
            _, rel = q["entity_ids"]["subject"], q["entity_ids"]["relation"]
            by_sub_rel[rel].append(k)

    return by_sub_rel


def partition_idx(by_question):
    by_idx = defaultdict(list)
    for k, v in by_question.items():
        for q in v:
            idx = q["idx"]
            by_idx[idx].append(k)

    return by_idx


def maybe_split(keys):
    split = keys.split("[SEP]")
    if len(split) == 2:
        return split[0].strip(), split[1].strip(), None
    elif len(split) == 3:
        return [s.strip() for s in split]
    else:
        print(keys)


def generate_answers(question_text, question_type, question_facts):
    assert all(q["qid"].startswith(question_type) for q in question_facts)
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
                    print(question)
                    print([a[1][0][0] for a in answers.items()])
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


def sample_databases(
    num_to_generate, db_target_size, partitioned_questions, by_question
):
    num_generated = 0
    while num_generated < num_to_generate:
        num_generated += 1
        db = []

        # Iterate through questions and make DBs containing facts only
        while len(db) < db_target_size:
            current_indexes = set(f["idx"] for f in db)

            # First pick whether we are adding a singleton, short, medium or long query
            question_set = random.choices(partitioned_questions, weights=sample_probs)[
                0
            ]

            if len(question_set):
                # Pick a question from that set and add all facts to the DB
                sampled_question = random.choice(question_set)
                sampled_facts = random.sample(
                    by_question[sampled_question],
                    min(
                        25, db_target_size - len(db), len(by_question[sampled_question])
                    ),
                )

                # Don't add duplicate facts
                db.extend(
                    filter(lambda f: f["idx"] not in current_indexes, sampled_facts)
                )

        logger.info("Constructed DB of size {} queries".format(len(db)))
        yield db


def generate_facts_for_db(db):
    generated = {}
    generated["question_answers"] = []
    generated["question_derivations"] = []
    generated["question_facts"] = []
    generated["question_types"] = []
    generated["questions"] = []
    generated["heights"] = []
    generated["rels"] = []

    generated["indexes"] = set(f["idx"] for f in db)
    generated["qids"] = set(f["qid"] for f in db)
    generated["subjects"] = set(f["entity_ids"]["subject"] for f in db)
    generated["relations"] = set(f["entity_ids"]["relation"] for f in db)
    generated["subj_rels"] = set(
        (f["entity_ids"]["subject"], f["entity_ids"]["relation"]) for f in db
    )

    # Store the list of questions we are gonna make queries over
    logger.info("Add positive facts (with original questions)")
    active_questions = defaultdict(list)
    for query in db:
        active_questions[query["qid"]].append(query)

    # Then add negative facts (facts which have no questions)
    logger.info("Add negative facts (without questions)")
    alternative_subjects = random.sample(
        set(by_subj.keys()).difference(), db_target_size
    )
    extra_negative_facts_ids = set()
    extra_negative_facts = []
    for subj in alternative_subjects:
        additional_qs = by_subj[subj]
        extra_negative_queries = list(
            filter(
                lambda r: r.split("_")[1] not in generated["relations"],
                random.sample(additional_qs, min(len(additional_qs), 100)),
            )
        )
        for q in extra_negative_queries:
            questions = by_question[q]
            found = random.choice(questions)
            if found["idx"] not in extra_negative_facts_ids:
                extra_negative_facts.append(found)
                extra_negative_facts_ids.add(found["idx"])

    negative_facts_to_add = args.extra_negative_facts

    logger.info(f"Adding {len(extra_negative_facts)} extras")
    if len(extra_negative_facts):
        db.extend(
            random.sample(
                extra_negative_facts,
                min(len(extra_negative_facts), negative_facts_to_add),
            )
        )

    # Make an ordering of the facts that the instances will be inserted in
    logger.info("Generate random order DB")
    random.shuffle(db)
    ordering = [f["idx"] for f in db]

    resc_qids = set()

    # For the active questions, generate positive answers over the entire DB
    logger.info("Generate positive answers")
    for qid, q in active_questions.items():
        resc_qids.add(qid)
        question_texts = [question["generated"]["question"] for question in q]
        fact_ids = [ordering.index(question["idx"]) for question in q]
        question_text = random.choice(question_texts)
        question_type = q[0]["template"]["question_type"]
        positive_answers = generate_answers(question_text, question_type, q)
        generated["question_answers"].append(positive_answers)
        generated["question_derivations"].append(
            [question["generated"]["derivation"] for question in q]
        )
        generated["question_facts"].append(fact_ids)
        generated["question_types"].append(question_type)
        generated["questions"].append(question_text)
        generated["heights"].append(len(db))
        generated["rels"].append([question["entity_ids"]["relation"] for question in q])

    # For the active facts (used by these questions), make a list of indexes being used
    additional_ids = set()
    for idx in generated["indexes"]:
        questions = by_idx[idx]
        for question in questions:
            extra_facts = by_question[question]
            additional_ids.update([fact["qid"] for fact in extra_facts])

        additional_ids = additional_ids.difference(generated["qids"])

    # Generate extra questions for these facts

    logger.info("Generate bonus answers")
    for qid in additional_ids:
        extra = [a for a in by_question[qid] if a["idx"] in generated["indexes"]]
        if len(extra) and random.uniform(0, 1) < 0.2:
            resc_qids.add(qid)
            fact_ids = [ordering.index(question["idx"]) for question in extra]
            question_text = random.choice([e["generated"]["question"] for e in extra])
            positive_answers = generate_answers(
                question_text, extra[0]["template"]["question_type"], extra
            )
            #
            # if "TRUE" in positive_answers:
            #     continue

            generated["question_answers"].append(positive_answers)
            generated["question_derivations"].append(
                [question["generated"]["derivation"] for question in extra]
            )
            generated["question_facts"].append(fact_ids)
            generated["question_types"].append(extra[0]["template"]["question_type"])
            generated["questions"].append(question_text)
            generated["heights"].append(len(db) - 1)
            generated["rels"].append(
                [question["entity_ids"]["relation"] for question in extra]
            )

    # Do the same for each subset of the database
    tmp_positive_answers = []
    tmp_fact_ids = []
    tmp_derivations = []
    tmp_types = []
    tmp_questions = []
    tmp_rels = []
    tmp_heights = []

    logger.info("Generate bonus answers for smaller DBs")
    for i in range(len(ordering)):
        collected_indexes = set(ordering[:i])

        for qid in resc_qids:
            facts = by_question[qid]
            filtered_facts = [
                a
                for a in facts
                if a["idx"] in generated["indexes"] and a["idx"] in collected_indexes
            ]

            question_text = random.choice([f["generated"]["question"] for f in facts])
            question_type = facts[0]["template"]["question_type"]

            tmp_fact_ids.append(
                [ordering.index(fact["idx"]) for fact in filtered_facts]
            )
            tmp_positive_answers.append(
                generate_answers(question_text, question_type, filtered_facts)
            )
            tmp_derivations.append(
                [fact["generated"]["derivation"] for fact in filtered_facts]
            )
            tmp_heights.append(i)
            tmp_types.append(question_type)
            tmp_questions.append(question_text)
            tmp_rels.append([fact["entity_ids"]["relation"] for fact in filtered_facts])

    extended_question_answers = []
    master_answers = set(
        linearize(a) for a in zip(generated["questions"], generated["question_answers"])
    )
    for qidx, (question, answer, qtype, height) in enumerate(
        zip(tmp_questions, tmp_positive_answers, tmp_types, tmp_heights)
    ):
        sample_prob = 0.05 if linearize((question, answer)) in master_answers else 0.3
        if None in answer:
            sample_prob += 0.0
        elif qtype == "argmin" or qtype == "argmax" or qtype == "min" or qtype == "max":
            sample_prob += 0.4

        if height < 4:
            sample_prob = 0.001  # max(0.001, sample_prob - 0.2)

        if random.uniform(0, 1) <= sample_prob:
            extended_question_answers.append(qidx)

    for eq in extended_question_answers:
        generated["question_answers"].append(tmp_positive_answers[eq])
        generated["question_derivations"].append(tmp_derivations[eq])
        generated["question_facts"].append(tmp_fact_ids[eq])
        generated["question_types"].append(tmp_types[eq])
        generated["questions"].append(tmp_questions[eq])
        generated["rels"].append(tmp_rels[eq])
        generated["heights"].append(tmp_heights[eq])

    # Go through all generated questions/answers and zip them together
    generated["qs"] = []
    for question, answer, qtype, fact, derivation, height, rel in zip(
        generated["questions"],
        generated["question_answers"],
        generated["question_types"],
        generated["question_facts"],
        generated["question_derivations"],
        generated["heights"],
        generated["rels"],
    ):
        if len(fact) != len(set(fact)):
            continue
        # For all DB of facts, then create the questions and answers associated with that question
        generated["qs"].append(
            {
                "question": question.strip().replace("Whow many", "How many"),
                "answer": answer,
                "type": qtype,
                "facts": fact,
                "deriations": derivation,
                "height": height,
                "relation": rel,
            }
        )

    generated["facts"] = [q["instance"]["candidate"].strip() for q in db]
    logger.info(f"Added {len(generated['qs'])} queries to DB")
    return generated


def generate_db_facts(dbs):
    for db in dbs:
        try:
            generated = generate_facts_for_db(db)
            yield generated
        except Exception as e:
            logger.error(e)


if __name__ == "__main__":
    setup_logging()

    parser = ArgumentParser()
    parser.add_argument("questions_file")
    parser.add_argument("out_file")
    parser.add_argument(
        "--size", help="Target size of facts in DB", type=int, default=50
    )
    parser.add_argument(
        "--extra_negative_facts",
        help="Extra negative facts to add to DB",
        type=int,
        default=10,
    )
    parser.add_argument(
        "--num_to_make", help="Target size of facts in DB", type=int, default=5
    )
    parser.add_argument(
        "--short",
        help="Questions over <N of these facts (but >2) will be labeled as short questions.",
        type=int,
        default=5,
    )
    parser.add_argument(
        "--long",
        help="Questions>M (but <M) with be labeled as long questions",
        type=int,
        default=10,
    )
    parser.add_argument(
        "--weights",
        help="Sample weights for size of queries (short, medium, long). "
        "The rest is padded with singletons",
        type=float,
        nargs=3,
        default=[0.3, 0.1, 0.1],
    )

    args = parser.parse_args()
    logger.info(repr(args))

    db_target_size = args.size
    num_dbs_to_make = args.num_to_make

    # First set the sample weights and make sure that they add up to 1
    singleton_prob = 1 - np.sum(args.weights)
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
    with open(args.out_file, "w+") as of:
        for db in generate_db_facts(
            sample_databases(
                num_dbs_to_make,
                db_target_size - args.extra_negative_facts,
                partitioned_questions,
                by_question,
            )
        ):

            for q in db["qs"]:
                stats_type[q["type"]] += 1
                stats_lens[len(q["facts"])] += 1

            ret_obj = {"facts": db["facts"], "queries": db["qs"]}

            of.write(json.dumps(ret_obj) + "\n")

    print(stats_type)
    print(stats_lens)
