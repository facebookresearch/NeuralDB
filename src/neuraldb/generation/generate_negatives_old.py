import json
import copy
import random
from collections import defaultdict
from functools import partial, lru_cache
import sqlite3
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool

from tqdm import tqdm


def generate(positive, extra, k=1):
    if len(extra) == 0:
        return None

    pos = random.randint(0, len(extra) - 1)
    negative = extra[pos]
    # for negative in random.sample(extra,k=min(k, len(extra)) ):
    yield {
        "fact": negative["fact"],
        "query": positive["query"],
        "projection": None,
        "prop": negative["prop"],
        "subject": negative["subject"],
        "object": negative["object"],
        "type": "negative({})".format(positive["type"]),
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


def get_negatives_for(instance, by_prop, by_subject, by_object, k=1):
    negatives = []
    same_prop = list(
        filter(
            lambda prop: prop["subject"] != instance["subject"]
            and prop["object"] != instance["object"],
            by_prop[instance["prop"]],
        )
    )

    same_subject = list(
        filter(
            lambda prop: prop["object"] != instance["object"],
            by_subject[instance["subject"]],
        )
    )

    same_object = list(
        filter(
            lambda prop: prop["subject"] != instance["subject"],
            by_object[instance["object"]],
        )
    )

    other_types = list(filter(lambda k: k != instance["prop"], by_prop.keys()))

    if len(other_types):
        rand_type = random.sample(other_types, k=1)

        diff_prop1 = get_matching(rand_type[0], instance["subject"], instance["object"])
        diff_prop2 = get_mismatching(
            rand_type[0], instance["subject"], instance["object"]
        )

        negatives.extend(generate(instance, diff_prop1, k=k))
        negatives.extend(generate(instance, diff_prop2, k=k))

    negatives.extend(generate(instance, same_prop, k=k))
    negatives.extend(generate(instance, same_subject, k=k))
    negatives.extend(generate(instance, same_object, k=k))

    return instance, random.sample(negatives, k=k)


def get_negatives_for_db(instance, cursor, k=1):

    action = random.randint(0, 2)

    if action == 0:
        same_prop = cursor.execute(
            "SELECT * FROM instances "
            "WHERE subject != :subject AND object != :object  AND prop = :prop",
            instance,
        ).fetchall()
        if len(same_prop):
            return instance, random.sample(list(generate(instance, same_prop)), k=k)

    elif action == 1:
        same_prop = cursor.execute(
            "SELECT * FROM instances " "WHERE subject = :subject AND object != :object",
            instance,
        ).fetchall()
        if len(same_prop):
            return instance, random.sample(list(generate(instance, same_prop)), k=k)
    elif action == 2:
        same_prop = cursor.execute(
            "SELECT * FROM instances " "WHERE subject != :subject AND object = :object",
            instance,
        ).fetchall()
        if len(same_prop):
            return instance, random.sample(list(generate(instance, same_prop)), k=k)

    return instance, []
    # other_types = list(filter(lambda k: k != instance["prop"], by_prop.keys()))

    # if len(other_types):
    #    rand_type = random.sample(other_types, k=1)


#
#    diff_prop1 = get_matching(rand_type[0], instance["subject"], instance["object"])
#    diff_prop2 = get_mismatching(rand_type[0], instance["subject"], instance["object"])

#    negatives.extend(generate(instance, diff_prop1,k=k))
#    negatives.extend(generate(instance, diff_prop2,k=k))


def get_instances():
    with open("positive_data.jsonl") as f:
        for line in f:
            yield json.loads(line)


if __name__ == "__main__":

    by_prop = defaultdict(list)
    by_subject = defaultdict(list)
    by_object = defaultdict(list)

    instances = list(tqdm(get_instances()))

    conn = sqlite3.connect(":memory:")
    conn.isolation_level = None
    cursor = conn.cursor()
    cursor.arraysize = 1000

    print("Create table")
    cursor.execute(
        "CREATE TABLE instances (fact,query,projection,prop,subject,object,type);"
    )
    conn.commit()

    print("Insert data")
    conn.executemany(
        "INSERT INTO instances (fact, query, projection, prop, subject, object, type) "
        "VALUES (:fact,:query,:projection,:prop,:subject,:object,:type)",
        instances,
    )
    conn.commit()

    print("Build indexes")
    cursor.execute("CREATE INDEX idx_prop ON instances (prop);")
    cursor.execute("CREATE INDEX idx_subject ON instances (subject);")
    cursor.execute("CREATE INDEX idx_object ON instances (object);")
    cursor.execute("CREATE INDEX idx_type ON instances (type);")
    cursor.execute("CREATE INDEX idx_subj_obj ON instances (subject,object);")
    cursor.execute("CREATE INDEX idx_prop_subj_obj ON instances (prop,subject,object);")
    conn.commit()

    get_negatives = partial(get_negatives_for_db, cursor=cursor)
    out_data = []

    pool = ThreadPool()
    for pos_example, negative_examples in tqdm(
        map(get_negatives, instances), total=len(instances)
    ):
        out_data.append(pos_example)
        out_data.extend(negative_examples)

    with open("generated_data.jsonl", "w+") as of:
        for line in out_data:
            of.write(json.dumps(line) + "\n")
