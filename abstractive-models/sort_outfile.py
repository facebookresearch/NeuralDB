import json
import sys


def read_ndb_gold(file):
    gold_data = json.load(open(file))
    sources = []
    targets = []
    for i in range(len(gold_data)):
        targets.extend([g[2] for g in gold_data[i]['queries']])
        sources.extend([g[1] for g in gold_data[i]['queries']])
    return sources, targets


def ndb_reorder(file, gold):
    with open(file, "r") as f:

        for line in f.readlines():
            qa = json.loads(line)

            ids = qa['id']
            output = qa['queries']
            if len(output) == 0:
                continue

    g_sources, g_targets = read_ndb_gold(gold)

    data = []
    for i, q_s in enumerate(g_sources):
        index = ids.index(i + 1)

        if index < 0:
            print(i, q_s)
        data.append(output[index])

    qs = {'queries': data}
    with open(file + "_reordered", "w") as f:
        json.dump(qs, f)


gold = sys.argv[1]
guess = sys.argv[2]

ndb_reorder(guess, gold)
