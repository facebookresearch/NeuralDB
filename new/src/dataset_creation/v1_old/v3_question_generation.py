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


def substitute(q, subject_name, formatted_object, rel):
    return q.replace("$s", subject_name).replace("$o", formatted_object) if rel not in ["P35"] else q.replace("$o", subject_name).replace("$s", formatted_object)



def generate(wikidata , final_templates):
    relations_cache = dict()
    for subject in wikidata.collection.find():
        subject_name = subject['english_name']

        if subject_name is None:
            continue

        for rel in set(subject['property_types']).intersection(final_templates.keys()):
            if rel not in relations_cache:
                relations_cache[rel] = wikidata.get_by_id_or_uri(rel)['english_name']

            for object_data, object_metadata in subject['properties'][rel]:
                if object_data is None:
                    continue

                formatted_object = ''
                if 'id' in object_data:
                    if object_data['id'] is None:
                        continue
                    retrieved_object = wikidata.get_by_id_or_uri(object_data['id'])

                    if retrieved_object is None:
                        continue

                    formatted_object = retrieved_object['english_name']

                elif 'unit' in object_data:
                    if object_data['unit'] is None or object_data['amount'] is None:
                        continue

                    if object_data["unit"].startswith("http"):
                        ulookup = wikidata.get_by_id_or_uri(object_data['unit'])
                        if ulookup is None:
                            continue

                        formatted_object = object_data['amount'] + " " + ulookup['english_name']
                    else:
                        formatted_object = object_data['unit'] if object_data['unit'] != "1" else ""
                else:
                    formatted_object = ""

                if formatted_object is None or not formatted_object:
                    continue

                template = final_templates[rel]
                available_question_types = list(set(template.keys()).difference({"fact", "_subject", "_object"}))

                for question_type in available_question_types:
                    question_template = random.choice(template[question_type])
                    generated = {
                        "output": [substitute(q,subject_name,formatted_object,rel) for q in
                                   question_template],
                        "input": [question_type, subject_name, relations_cache[rel], formatted_object],
                        "metadata": {"subject": subject["wikidata_id"], "object": object_data, "relation": rel,
                                     "question_type": question_type, "template": question_template}
                    }
                    yield generated


if __name__ == "__main__":
    wikidata = Wikidata()
    parser = ArgumentParser()
    parser.add_argument("out_file")
    args = parser.parse_args()

    skip = {"is","a","of","between","on","in"}

    with open("generate_v1.5.json") as f:
        final_templates = json.load(f)

    with open(args.out_file, "w+") as f:
        for instance in tqdm(generate(wikidata, final_templates)):
            f.write(json.dumps(instance)+"\n")

    # for rel, templates in final_templates.items():
    #     a = wikidata.get_by_id_or_uri(rel)
    #     matching = wikidata.find_matchilng_relation(rel)
    #     for subject in matching:
    #         for object in subject['properties'][rel]:
    #             pass

