import json
import copy
import random
import sys
from collections import defaultdict
from functools import partial, lru_cache
import sqlite3
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool

from tqdm import tqdm


def generate(positive, extra):
    if len(extra) == 0:
        return None

    for negative in extra:
        # for negative in random.sample(extra,k=min(k, len(extra)) ):
        # yield {
        #     "fact": negative[0],
        #     "query": positive["query"],
        #     "projection": None,
        #     "prop": negative[3],
        #     "subject": negative[4],
        #     "object": negative[5],
        #     "type": "negative({})".format(positive["type"])
        # }
        yield {
            "fact": negative["fact"],
            "query": positive["query"],
            "projection": None,
            "prop": negative["prop"],
            "subject": negative["subject"],
            "object": negative["object"],
            "extra_subject": positive["subject"],
            "extra_object": positive["object"],
            "type": "negative({},{})".format(negative["type"], positive["type"]),
        }


@lru_cache(maxsize=99999999)
def get_matching(rand_prop, subject, object):
    return list(
        filter(
            lambda prop: prop["subject"] == subject or prop["object"] == object,
            random.sample(by_prop[rand_prop], k=10),
        )
    )


@lru_cache(maxsize=99999999)
def get_mismatching(rand_prop, subject, object):
    return list(
        filter(
            lambda prop: prop["subject"] != subject and prop["object"] != object,
            random.sample(by_prop[rand_prop], k=10),
        )
    )


def sample_one_of_subject_or_object_match(instances, subject, object, ttl=100):
    if ttl <= 0 or len(instances) == 0:
        return []

    sampled = random.choice(instances)
    if sampled["subject"] == subject or sampled["object"] == object:
        return [sampled]
    else:
        return sample_one_of_subject_or_object_match(
            instances, subject, object, ttl - 1
        )


def sample_no_subject_or_object_match(instances, subject, object, ttl=100):
    if ttl <= 0 or len(instances) == 0:
        return []

    sampled = random.choice(instances)
    if sampled["subject"] == subject or sampled["object"] == object:
        return sample_no_subject_or_object_match(instances, subject, object, ttl - 1)
    else:
        return [sampled]


def sample_no_object_match(instances, object, ttl=100):
    if ttl <= 0 or len(instances) == 0:
        return []

    sampled = random.choice(instances)
    if sampled["object"] == object:
        return sample_no_object_match(instances, object, ttl - 1)
    else:
        return [sampled]


def sample_no_subject_match(instances, subject, ttl=100):
    if ttl <= 0 or len(instances) == 0:
        return []

    sampled = random.choice(instances)
    if sampled["subject"] == subject:
        return sample_no_subject_match(instances, subject, ttl - 1)
    else:
        return [sampled]


def sample_anything(instances, ttl=100):
    if ttl <= 0 or len(instances) == 0:
        return []

    sampled = random.choice(instances)
    return [sampled]


def get_negatives_for(instance, by_prop, by_subject, by_object, k=1):
    negatives = []
    samples = []

    # If query has both the subject and object in it
    #  - We have the best freedom for negative instances as we can switch subject or object
    # "symmetric" in instance and (instance["object"] in instance["query"] or instance["subject"] in instance["query"])):
    if (
        instance["object"] in instance["query"]
        and instance["subject"] in instance["query"]
    ):
        samples.extend(sample_anything(by_prop[instance["prop"]]))

    # If query has the object but not the subject in it
    elif instance["object"] in instance["query"]:
        samples.extend(
            sample_no_object_match(by_prop[instance["prop"]], instance["object"])
        )

    # If query has the subject but not the object in it
    elif instance["subject"] in instance["query"]:
        samples.extend(
            sample_no_subject_match(by_prop[instance["prop"]], instance["object"])
        )

    # If query has neither subject or object in it, then it shouldn't be replaced with the same prop as
    # it covers everything
    else:
        pass

    diff_samples = []
    other_types = list(
        filter(
            lambda k: k != instance["prop"]
            and ("mutex" not in instance or k not in instance["mutex"]),
            by_prop.keys(),
        )
    )
    if len(other_types):
        rand_type = random.sample(other_types, k=1)
        diff_samples.extend(
            sample_no_subject_or_object_match(
                by_prop[rand_type[0]], instance["subject"], instance["object"]
            )
        )
        diff_samples.extend(
            sample_one_of_subject_or_object_match(
                by_prop[rand_type[0]], instance["subject"], instance["object"]
            )
        )

    if len(diff_samples) == 0 and len(samples) > 0:
        negatives.extend(generate(instance, samples))
    elif len(samples) == 0 and len(diff_samples) > 0:
        negatives.extend(generate(instance, diff_samples))
    elif len(samples) == 0 and len(diff_samples) == 0:
        return instance, []
    else:
        i = random.randint(0, 1)
        if i:
            negatives.extend(generate(instance, diff_samples))
        else:
            negatives.extend(generate(instance, samples))

    return instance, random.sample(negatives, k=k)


def get_instances():
    with open("positive_data.jsonl") as f:
        for line in f:
            yield json.loads(line)


if __name__ == "__main__":

    by_prop = defaultdict(list)
    by_subject = defaultdict(list)
    by_object = defaultdict(list)

    instances = list(tqdm(get_instances()))
    for instance in instances:
        by_prop[instance["prop"]].append(instance)
        by_subject[instance["subject"]].append(instance)
        by_object[instance["object"]].append(instance)

    samples1 = []
    samples2 = []
    samples3 = []
    for instance in instances:
        if (
            instance["object"] in instance["query"]
            and instance["subject"] in instance["query"]
        ):
            samples1.extend(sample_anything(by_prop[instance["prop"]]))

        # If query has the object but not the subject in it
        elif instance["object"] in instance["query"]:
            samples2.extend(
                sample_no_object_match(by_prop[instance["prop"]], instance["object"])
            )

        # If query has the subject but not the object in it
        elif instance["subject"] in instance["query"]:
            samples3.extend(
                sample_no_subject_match(by_prop[instance["prop"]], instance["object"])
            )

    for i in random.sample(samples1, 10):
        print(i)
    print("-" * 100)
    for i in random.sample(samples2, 10):
        print(i)

    print("-" * 100)
    for i in random.sample(samples3, 10):
        print(i)

    get_negatives = partial(
        get_negatives_for, by_prop=by_prop, by_subject=by_subject, by_object=by_object
    )
    out_data = []

    for pos_example, negative_examples in tqdm(
        map(get_negatives, instances), total=len(instances)
    ):
        out_data.append(pos_example)
        out_data.extend(negative_examples)

    with open("generated_data.jsonl", "w+") as of:
        for line in out_data:

            of.write(json.dumps(line) + "\n")
