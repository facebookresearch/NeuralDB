import json
import math
import random
import numpy as np
from argparse import ArgumentParser
from collections import defaultdict
from nltk import word_tokenize
from nltk import ngrams
from nltk.tokenize.treebank import TreebankWordDetokenizer
from similarity.normalized_levenshtein import NormalizedLevenshtein
from tqdm import tqdm
from wikidata_common.wikidata import Wikidata

detok = TreebankWordDetokenizer()


def generate_hypotheses(instance):
    for s,r,o in instance['valid_hypotheses']:
        if r not in final_templates:
            continue
        yield (s,r,o)


def normalize_subject(subject_name,fact):
    if subject_name is None:
        return None

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
        fact = detok.detokenize(fact.split()).replace(" 's", "'s").replace(
            " ,", ",")

        if subject_name not in fact:
            return None

        assert subject_name in fact, f"Subject {subject_name} was not in {fact}"
    return fact


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    parser.add_argument("--num_dbs_to_make", type=int, default=1000)
    parser.add_argument("--sample_rels", type=int, default=4)
    parser.add_argument("--sample_per_rel", type=int, default=10)
    parser.add_argument("--sample_extra", type=int, default=5)
    parser.add_argument("--estimated_size", type=int, default=14300808)
    args = parser.parse_args()

    wiki = Wikidata()
    loaded = []
    by_subject = defaultdict(list)
    by_relation = defaultdict(list)
    by_object = defaultdict(list)

    with open("generate_v1.5.json") as f:
        final_templates = json.load(f)

    # print(final_templates.keys())
    with open(args.in_file) as f:
        for ix, line in enumerate(tqdm(f,total=args.estimated_size)):
            instance = json.loads(line)
            added_id = None

            # Check if it contains a relation we care about
            for s,r,o in generate_hypotheses(instance):
                if added_id is None:
                    added_id = len(loaded)
                    loaded.append(instance)

            # If it doesn't skip this claim
            if added_id is None:
                continue

            # Correct the claim
            fact = instance['candidate'].strip()
            for s,r,o in generate_hypotheses(instance):
                name = wiki.get_by_id_or_uri(s)['english_name']

                if name is None:
                    fact = None
                    break

                fact = normalize_subject(name, fact)

                if fact is None:
                    break

                if o.startswith("Q"):
                    name = wiki.get_by_id_or_uri(o)['english_name']
                    if name is None:
                        fact = None
                        break

                    fact = normalize_subject(name, fact)

                if fact is None:
                    break

            instance['fact'] = fact
            if fact is None or "⁇" in fact:
                continue

            # Add the filtered relations to the dictionaries
            for s,r,o in generate_hypotheses(instance):
                by_subject[s].append(added_id)
                by_relation[r].append(added_id)
                by_object[o].append(added_id)

    with(open("generate_cache.json","w+")) as f:
        json.dump({
            "loaded": loaded,
            "by_subject": by_subject,
            "by_object": by_object,
            "by_relation": by_relation
        },f)

    all_subjects = list(by_subject.keys())
    all_relations = list(by_relation.keys())
    all_objects = list(by_object.keys())

    print(len(all_subjects),len(all_objects), len(all_relations))

    # Make train/dev/test split
    number_to_make = dict()
    number_to_make["train"] = args.num_dbs_to_make
    number_to_make["dev"] = args.num_dbs_to_make //10
    number_to_make["test"] = args.num_dbs_to_make //10

    all_entities = list(set(all_subjects).union(set(all_objects)))
    random.shuffle(all_entities)

    split_subjects = defaultdict(list)
    split_objects = defaultdict(list)
    split_by_relation = defaultdict(lambda: defaultdict(list))

    p1 = math.floor(len(all_entities)*.7)
    p2 = math.floor(len(all_entities)*.85)
    tr,de,te = all_entities[:p1], all_entities[p1:p2], all_entities[p2:]

    split_subjects["train"] = set([a for a in tr if a in by_subject])
    split_subjects["dev"] = set([a for a in de if a in by_subject])
    split_subjects["test"] = set([a for a in te if a in by_subject])

    split_objects["train"] = set([a for a in tr if a in by_object])
    split_objects["dev"] = set([a for a in de if a in by_object])
    split_objects["test"] = set([a for a in te if a in by_object])

    for split in ["train","dev","test"]:
        for rel,facts in by_relation.items():
            split_by_relation[split][rel].extend([f for f in facts if
                                             all(h[0] in split_subjects[split] for h in loaded[f]['valid_hypotheses'])
                                             # and all(h[2] in split_objects[split] for h in loaded[f]['valid_hypotheses'])
                                             ])
    print([(k, len(v)) for k, v in split_by_relation["train"].items()])
    print([(k, len(v)) for k, v in split_by_relation["dev"].items()])
    print([(k, len(v)) for k, v in split_by_relation["test"].items()])


    for split in ["train","dev","test"]:
        with open(args.out_file+"_"+split, "w+") as of:
            for db_id in range(number_to_make[split]):
                # print(f"Building database {db_id}")

                new_db_fact_ids = set()

                db_subjs = random.sample(split_subjects[split], k=args.sample_extra)
                db_objs = random.sample(split_objects[split], k=args.sample_extra)
                db_rels = random.sample(all_relations, k=args.sample_rels)

                for fact in db_subjs:
                    new_db_fact_ids.update(by_subject[fact])

                for fact in db_objs:
                    new_db_fact_ids.update(by_object[fact])

                for rel in db_rels:
                    new_db_fact_ids.update(random.sample(split_by_relation[split][rel],k=min(len(split_by_relation[split][rel]),args.sample_per_rel)))

                db = [loaded[idx] for idx in new_db_fact_ids]
                of.write(json.dumps(db)+"\n")



