import json
from collections import defaultdict

import numpy as np
from argparse import ArgumentParser
from nltk import ngrams
from nltk import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from similarity.normalized_levenshtein import NormalizedLevenshtein
from tqdm import tqdm

from ndb_data.wikidata_common.wikidata import Wikidata

detok = TreebankWordDetokenizer()


def generate_hypotheses(instance):
    for s, r, o in instance["valid_hypotheses"]:
        if r not in final_templates:
            continue
        yield (s, r, o)


def normalize_subject(subject_name, fact):
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
        fact = detok.detokenize(fact.split()).replace(" 's", "'s").replace(" ,", ",")

        if subject_name not in fact:
            return None

        assert subject_name in fact, f"Subject {subject_name} was not in {fact}"
    return fact


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    parser.add_argument("--estimated_size", type=int)
    args = parser.parse_args()

    wiki = Wikidata()
    loaded = []
    by_subject = defaultdict(list)
    by_relation = defaultdict(list)
    by_object = defaultdict(list)

    with open("configs/generate_v1.5.json") as f:
        final_templates = json.load(f)

    # print(final_templates.keys())
    with open(args.in_file) as f:
        for ix, line in enumerate(tqdm(f, total=args.estimated_size)):
            instance = json.loads(line)
            added_id = None

            # Check if it contains a relation we care about
            for s, r, o in generate_hypotheses(instance):
                if added_id is None:
                    added_id = len(loaded)
                    loaded.append(instance)

            # If it doesn't skip this claim
            if added_id is None:
                continue

            # Correct the claim
            fact = instance["candidate"].strip()
            for s, r, o in generate_hypotheses(instance):
                name = wiki.get_by_id_or_uri(s)["english_name"]

                if name is None:
                    fact = None
                    break

                fact = normalize_subject(name, fact)

                if fact is None:
                    break

                if o.startswith("Q"):
                    name = wiki.get_by_id_or_uri(o)["english_name"]
                    if name is None:
                        fact = None
                        break

                    fact = normalize_subject(name, fact)

                if fact is None:
                    break

            instance["fact"] = fact
            if fact is None or "⁇" in fact:
                continue

            # Add the filtered relations to the dictionaries
            for s, r, o in generate_hypotheses(instance):
                by_subject[s].append(added_id)
                by_relation[r].append(added_id)
                by_object[o].append(added_id)

    with (open(args.out_file, "w+")) as f:
        json.dump(
            {
                "loaded": loaded,
                "by_subject": by_subject,
                "by_object": by_object,
                "by_relation": by_relation,
            },
            f,
        )
