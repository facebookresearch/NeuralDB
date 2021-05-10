import bz2
import glob
import json
import pprint
import datetime as dt
import itertools
import random
import logging
from multiprocessing.pool import ThreadPool
from functools import partial
from log_helper import setup_logging
import json
from collections import defaultdict
from tqdm import tqdm

import requests


def req_patch(self, *args, **kwargs):
    timeout = kwargs.pop("timeout", 2)
    return self.request_orig(*args, **kwargs, timeout=timeout)


setattr(requests.sessions.Session, "request_orig", requests.sessions.Session.request)
requests.sessions.Session.request = req_patch

pp = pprint.PrettyPrinter()
logger = logging.getLogger(__name__)


def try_read_line(filename):
    with bz2.open(filename, mode="rt") as f:
        f.read(2)
        for line in f:
            yield line


def try_parse_line(line):
    try:
        return json.loads(line.rstrip(",\n"))
    except json.decoder.JSONDecodeError:
        pass


def open_wikidata(pool, filename):
    return filter(
        lambda line: line is not None,
        pool.imap(try_parse_line, try_read_line(filename)),
    )


def process_rule(rule, subject, object):
    return rule.replace("$s", subject).replace("$o", object)


def get_best_subject(claim):
    return (
        clean_uri(claim["subject"]["uri"])
        if "uri" in claim["subject"] and claim["subject"] is not None
        else claim["subject"]["surfaceform"]
    )


def get_best_object(claim):
    return (
        clean_uri(claim["object"]["uri"])
        if "uri" in claim["object"] and claim["object"] is not None
        else claim["object"]["surfaceform"]
    )


def generate_facts(claim, record, rules):

    return list(
        filter(
            lambda item: item is not None,
            map(
                lambda rule: (
                    process_rule(
                        rule[0], get_best_subject(claim), get_best_object(claim)
                    ),
                    process_rule(
                        rule[1], get_best_subject(claim), get_best_object(claim)
                    ),
                )
                if not isinstance(rule, str)
                else process_rule(
                    rule, get_best_subject(claim), get_best_object(claim)
                ),
                rules,
            ),
        )
    )


def merge_dicts(a, b):
    return {**a, **b}


def get_sentence(record, sid):
    start, stop = record["sentences_boundaries"][sid]
    return record["text"][start:stop], start, stop


def generate_facts_for_claim(record, claim, generator):

    generated = merge_dicts(
        {
            key: generate_facts(claim, record, rules)
            for key, rules in generator.items()
            if not key.startswith("_")
        },
        {
            key: generated[0]
            for key, generated in (
                (key, generate_facts(claim, record, [rule]))
                for key, rule in generator.items()
                if key.startswith("_")
            )
            if len(generated)
        },
    )

    replacements = []

    if claim["subject"]["boundaries"] is not None:
        replacements.append(claim["subject"])

    if claim["object"]["boundaries"] is not None:
        replacements.append(claim["object"])

    replacements = sorted(replacements, key=lambda a: a["boundaries"][0], reverse=True)

    sent, start, stop = get_sentence(record, claim["sentence_id"])
    generated["fact"] = [sent]
    for replacement in replacements:
        generated["fact"][0] = (
            generated["fact"][0][: replacement["boundaries"][0] - start]
            + clean_uri(replacement["uri"])
            + generated["fact"][0][replacement["boundaries"][1] - start :]
        )

    return generated


def clean_uri(uri):
    return uri.replace("http://www.wikidata.org/prop/direct/", "").replace(
        "http://www.wikidata.org/entity/", ""
    )


def extract_facts_from_trex(record, generators):
    generated_items = []
    types = set()
    for idx, claim in enumerate(record["triples"]):
        key = clean_uri(claim["predicate"]["uri"])
        if key == "P31" and claim["object"]["uri"] is not None:
            types.add(clean_uri(claim["object"]["uri"]))

        if key in generators:
            generated_items.append(
                (
                    key,
                    "{}_{}".format(claim["sentence_id"], idx),
                    generate_facts_for_claim(record, claim, generators[key]),
                )
            )

    return generated_items


def open_trex(file):
    logger.info("Read {}".format(file))
    with open(file) as f:
        trex = json.load(f)
    return trex


if __name__ == "__main__":
    setup_logging()
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("generators")
    args = parser.parse_args()

    generated = defaultdict(dict)
    names = defaultdict(lambda: "[unresolved]")
    logger.info("Enumerating Trex files in directory {}".format(args.file))

    generators = json.load(open(args.generators))

    extracted = []

    # Go through every item and extract the generated fact, alternative names, and alternative types for
    # negative examples
    extractor = partial(extract_facts_from_trex, generators=generators)

    trex_files = glob.glob(args.file + "/*.json", recursive=False)

    # trex = open_trex(args.file)
    items = tqdm(
        map(
            extractor,
            itertools.chain.from_iterable(map(lambda f: open_trex(f), trex_files)),
        )
    )

    for extracted in items:
        for fact in extracted:
            relation, claim_id, generated_facts = fact
            generated[relation][claim_id] = generated_facts

    new_data = []
    for prop, mapped_claims in generated.items():
        logger.info("Generating facts for property {}".format(prop))

        for id, claim in mapped_claims.items():
            if "fact" not in claim or len(claim["fact"]) == 0:
                # print("Claim has zero facts")
                # pp.pprint(claim)
                continue

            fact = random.sample(claim["fact"], k=1)[0]

            subject = claim["_subject"]
            object = claim["_object"]

            for op in {
                "set",
                "argmin",
                "argmax",
                "count",
                "count_argmin",
                "count_argmax",
            }:
                if op in claim and len(claim[op]) > 0:
                    set_qa = random.sample(claim[op], k=1)[0]
                    set_q, set_a = set_qa

                    new_data.append(
                        json.dumps(
                            {
                                "fact": fact,
                                "query": set_q,
                                "projection": set_a,
                                "prop": prop,
                                "subject": subject,
                                "object": object,
                                "type": op,
                            }
                        )
                    )

            if "lookup" in claim and len(claim["bool"]) > 0:
                lookup_qa = random.sample(claim["bool"], k=1)[0]
                lookup_q, lookup_a = lookup_qa

                new_data.append(
                    json.dumps(
                        {
                            "fact": fact,
                            "query": lookup_q,
                            "projection": fact,
                            "prop": prop,
                            "subject": subject,
                            "object": object,
                            "type": "lookup",
                        }
                    )
                )

    with open("positive_data_trex.jsonl", "w+") as f:
        for item in tqdm(new_data, desc="Writing positive training data"):
            f.write(item + "\n")
