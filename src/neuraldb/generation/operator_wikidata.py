import bz2
import json
import pprint
import datetime as dt
import itertools
import random
import logging
from collections import defaultdict
from multiprocessing.pool import ThreadPool
from functools import reduce, partial

import pytz
from dateutil.parser import parse as parse_date
from tqdm import tqdm

from log_helper import setup_logging

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

def try_parse_date(qual):
    try:
        return parse_date(qual["datavalue"]["value"]["time"].replace("+", "").replace("-00", "-01"))
    except Exception as e:
        print(qual)
        return None


def check_qualifiers(claim):


    if "qualifiers" not in claim:
        return True

    # Start time
    if "P580" in claim["qualifiers"]:
        if any(
            try_parse_date(qual) is not None and
            dt.datetime.now(tz=pytz.UTC)
            <= try_parse_date(qual)
            for qual in claim["qualifiers"]["P580"]
        ):
            return False

    # End time
    if "P582" in claim["qualifiers"]:
        if any(
            try_parse_date(qual) is not None and
            dt.datetime.now(tz=pytz.UTC)
            >= try_parse_date(qual)
            for qual in claim["qualifiers"]["P582"]
        ):
            return False

    return True


def process_rule(rule, subject, object):
    return rule.replace("$s", subject).replace("$o", object)


def generate_facts(snak, record, rules):
    return list(
        filter(
            lambda item: item is not None,
            map(
                lambda rule: (
                    process_rule(
                        rule[0],
                        record["id"],
                        snak["datavalue"]["value"]["id"]
                        if "id" in snak["datavalue"]["value"]
                        else snak["datavalue"]["value"]["amount"].replace("+", ""),
                    )
                    if "datavalue" in snak
                    else None,
                    process_rule(
                        rule[1],
                        record["id"],
                        snak["datavalue"]["value"]["id"]
                        if "id" in snak["datavalue"]["value"]
                        else snak["datavalue"]["value"]["amount"].replace("+", ""),
                    )
                    if "datavalue" in snak
                    else None,
                )
                if not isinstance(rule, str)
                else process_rule(
                    rule,
                    record["id"],
                    snak["datavalue"]["value"]["id"]
                    if "id" in snak["datavalue"]["value"]
                    else snak["datavalue"]["value"]["amount"].replace("+", ""),
                )
                if "datavalue" in snak
                else None,
                rules,
            ),
        )
    )


def merge_dicts(a, b):
    return {**a, **b}


def generate_facts_for_claim(record, claim, generator):
    snak = claim["mainsnak"]
    return merge_dicts(
        {
            key: generate_facts(snak, record, rules)
            for key, rules in generator.items()
            if not key.startswith("_")
        },
        {
            key: generated[0]
            for key, generated in (
                (key, generate_facts(snak, record, [rule]))
                for key, rule in generator.items()
                if key.startswith("_")
            )
            if len(generated)
        },
    )


def extract_facts_from_entity(record, generators):
    generated_items = []
    types = set()
    for key, claims in record["claims"].items():
        if key == "P31":
            for claim in claims:
                types.add(claim["mainsnak"]["datavalue"]["value"]["id"])

        if key in generators:
            for claim in filter(check_qualifiers, claims):
                generated_items.append(
                    (
                        key,
                        claim["id"],
                        generate_facts_for_claim(record, claim, generators[key]),
                    )
                )

    al = set()
    name = None
    if "en" in record["labels"]:
        al.add(record["labels"]["en"]["value"])
        name = record["labels"]["en"]["value"]

    if "en" in record["aliases"]:
        al.update([alias["value"] for alias in record["aliases"]["en"]])

    return generated_items, (record["id"], name, al, types)


if __name__ == "__main__":
    setup_logging()
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("generators")
    parser.add_argument("--complete", action="store_true")
    args = parser.parse_args()

    pool1 = ThreadPool(processes=20)
    wikidata = open_wikidata(pool1, args.file)

    negative_examples = defaultdict(set)
    reverse_negative_examples = defaultdict(set)
    generated = defaultdict(dict)

    names = defaultdict(None)
    aliases = defaultdict(set)

    logger.info("Enumerating Wikidata dump file {}".format(args.file))

    generators = json.load(open(args.generators))

    extracted = []
    pool = ThreadPool(processes=10)

    # Go through every item and extract the generated fact, alternative names, and alternative types for
    # negative examples
    extractor = partial(extract_facts_from_entity, generators=generators)
    items = tqdm(pool.imap(extractor, itertools.islice(wikidata, int(1e6))))
    for extracted, metadata in items:
        record_id, name, alias_list, types = metadata
        if name is not None:
            names[record_id] = name
            aliases[record_id].update(alias_list)

        for fact in extracted:
            relation, claim_id, generated_facts = fact
            generated[relation][claim_id] = generated_facts

        negative_examples[record_id].update(types)

    # Write out the negative examples
    with open("entity_types.jsonl", "w+") as f:
        for k, v in tqdm(negative_examples.items(), desc="Writing entity type dict"):
            f.write(json.dumps({"key": k, "value": list(v)}) + "\n")

    # Write out the negative examples
    with open("entity_names.jsonl", "w+") as f:
        for k, v in tqdm(names.items(), desc="Writing entity names dict"):
            f.write(json.dumps({"key": "name." + k, "value": v}) + "\n")

        for k, v in tqdm(aliases.items(), desc="Writing entity alias dict"):
            f.write(json.dumps({"key": "alias." + k, "value": list(v)}) + "\n")

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

            for op in {"set", "argmin", "argmax", "count" ,"min","max"}:
                if op in claim and len(claim[op]) > 0:
                    if not args.complete:
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
                    else:
                        for set_q, set_a in claim[op]:
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

            if "bool" in claim and len(claim["bool"]) > 0:
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
                            "type": "bool",
                        }
                    )
                )

    with open("positive_data.jsonl", "w+") as f:
        for item in tqdm(new_data, desc="Writing positive training data"):
            f.write(item + "\n")

        # for question,subject,object in generated_lookup:
        #     try:
        #         candidates = [a for a in itertools.chain.from_iterable([reverse_negative_examples[n] for n in negative_examples[subject]]) if a != subject]
        #         for candidate in random.sample(candidates,k=100):
        #             new = question.replace("$s", names[candidate]).replace("$o", names[object])
        #             if new not in x_generated_lookup:
        #                 print(new + " FALSE")
        #                 break
        #
        #         candidates = [a for a in itertools.chain.from_iterable([reverse_negative_examples[n] for n in negative_examples[object]]) if a != object]
        #         for candidate in random.sample(candidates,k=100):
        #             new = question.replace("$s", names[candidate]).replace("$o", names[object])
        #             if new not in x_generated_lookup:
        #                 print(new + " FALSE")
        #                 break
        #
        #     except:
        #         pass
