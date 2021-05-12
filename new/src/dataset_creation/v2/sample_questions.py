import json
import random
from argparse import ArgumentParser
from collections import Counter, defaultdict

from tqdm import tqdm


def get_size_bin(query):
    for idx, size in enumerate(size_bins):
        if len(query) <= size:
            return idx
    return len(size_bins)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    args = parser.parse_args()

    size_bins = [0,1,2,4,8,16]

    dataset = []
    added = 0


    added_q_type_bin = defaultdict(list)
    all_questions_binned = defaultdict(list)
    counts_bins = defaultdict(int)
    counts_facts = defaultdict(int)
    with open(args.in_file) as f, open(args.out_file,"w+") as of:
        for db_idx,line in tqdm(enumerate(f)):
            instance = json.loads(line)
            instance["all_queries"] = instance["queries"]
            instance["queries"] = []

            for question_idx,question in enumerate(instance["all_queries"]):
                qrel = question["relation"]
                qtype = question["type"]
                qbin = get_size_bin(question['facts'])
                all_questions_binned[(qtype,qbin)].append((db_idx,question_idx))

    strata = list(all_questions_binned.keys())
    empty_bins = set()

    added_instances = []
    while len(empty_bins) < len(strata) //2:
        key = random.choice(strata)

        if len(all_questions_binned[key]):
            if key[1]<3 and random.randint(0,100) > 25:
                continue

            population = all_questions_binned[key]

            # Pop one from the population and add it to the dataset
            sample = population.pop(random.randint(0,len(population)-1))
            added_q_type_bin[key].append(sample)
            instance["queries"].append(sample)
            added += 1
            added_instances.append(sample)
            counts_bins[key[1]]+=1

        else:
            empty_bins.add(key)

    to_add = defaultdict(list)

    for db_idx,question_idx in added_instances:
        to_add[db_idx].append(question_idx)

    with open(args.in_file) as f, open(args.out_file,"w+") as of:
        for db_idx,line in tqdm(enumerate(f)):
            instance = json.loads(line)
            instance["all_queries"] = instance["queries"]
            instance["queries"] = []

            for question_idx,question in enumerate(instance["all_queries"]):
                if question_idx in to_add[db_idx]:
                    q_bin = get_size_bin(question['facts'])
                    if q_bin < 3 and random.randint(0, 100) > 15:
                        continue
                    if q_bin == 3 and random.randint(0, 100) > 20:
                        continue
                    if q_bin == 4 and random.randint(0, 100) > 50:
                        continue
                    if q_bin == 5 and random.randint(0, 100) > 75:
                        continue

                    counts_facts[len(question['facts'])]+=1
                    instance['queries'].append(question)

            of.write(json.dumps(instance)+"\n")

    for k,v in added_q_type_bin.items():
        print(k,len(v))
    print(added)
    # print(q_bin)
    # print(q_type)
    # print(q_type_bin)

    print("bins")
    for i in range(0,6):
        print(i,counts_bins[i])

    print("lens")
    for i in range(0,26):
        print(i,counts_facts[i])