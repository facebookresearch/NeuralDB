import glob
import json
import math
import random
from collections import Counter, defaultdict

if __name__ == "__main__":

    for file in glob.glob("v1.8_*_*_fix3"):
        cnts = Counter()
        cnts_types = Counter()

        qct = 0
        lct = 0

        if not ("100" in file or "250" in file):
            continue

        with open(file) as f:
            by_type = defaultdict(list)
            for idx,line in enumerate(f):
                instance = json.loads(line)
                lct += 1
                qct += len(instance["queries"])
                for q in instance["queries"]:
                    cnts[len(q["facts"])] += 1
                    cnts_types[q['type']] +=1
                    by_type[q['type']].append((idx,q))

        if "fix" not in file:
            complex_retain = []
            if cnts_types["count_complex_none"] > cnts_types["count_complex_ok"]:
                complex_retain.extend(random.sample(by_type["count_complex_none"], k=min(len(by_type["count_complex_none"]), cnts_types["count_complex_ok"])))
            else:
                complex_retain.extend(by_type["count_complex_none"])


            if cnts_types["bool_complex_none"] > cnts_types["bool_complex_ok"]:
                complex_retain.extend(random.sample(by_type["bool_complex_none"], k=min(len(by_type["bool_complex_none"]), cnts_types["bool_complex_ok"])))
            else:
                complex_retain.extend(by_type["bool_complex_none"])


            if cnts_types["set_complex_none"] > cnts_types["set_complex_ok"]:
                complex_retain.extend(random.sample(by_type["set_complex_none"], k=min(len(by_type["set_complex_none"]), cnts_types["set_complex_ok"])))
            else:
                complex_retain.extend(by_type["set_complex_none"])


            if cnts_types["argmin_complex_none"] > cnts_types["argmin_complex_ok"]:
                complex_retain.extend(random.sample(by_type["argmin_complex_none"], k=min(len(by_type["argmin_complex_none"]), cnts_types["argmin_complex_ok"])))
            else:
                complex_retain.extend(by_type["argmin_complex_none"])


            if cnts_types["argmax_complex_none"] > cnts_types["argmax_complex_ok"]:
                complex_retain.extend(random.sample(by_type["argmax_complex_none"], k=min(len(by_type["argmax_complex_none"]), cnts_types["argmax_complex_ok"])))
            else:
                complex_retain.extend(by_type["argmax_complex_none"])

            retain_by_idx = defaultdict(list)

            for idx, item in complex_retain:
                retain_by_idx[idx].append(item)

            with open(file) as f, open(file+"_fix","w+") as of:
                by_type = defaultdict(list)
                for idx, line in enumerate(f):
                    instance = json.loads(line)

                    new_queries = []
                    for q in instance["queries"]:
                        if q["type"] not in {"set","count","bool"}:
                            new_queries.append(q)

                    new_queries.extend(retain_by_idx[idx])
                    random.shuffle(new_queries)
                    instance["queries"] = new_queries

                    of.write(json.dumps(instance)+"\n")

        if "fix2" not in file:
            complex_retain = []
            if cnts_types["bool"] > (cnts_types["argmin"]+cnts_types['argmax'])*1.5:
                complex_retain.extend(random.sample(by_type["bool"], k=min(len(by_type["bool"]), math.floor((cnts_types["argmin"]+cnts_types['argmax'])*1.5))))
            else:
                complex_retain.extend(by_type["bool"])


            if cnts_types["set"] > (cnts_types["argmin"]+cnts_types['argmax'])*1.5:
                complex_retain.extend(random.sample(by_type["set"], k=min(len(by_type["set"]), math.floor((cnts_types["argmin"]+cnts_types['argmax'])*1.5))))
            else:
                complex_retain.extend(by_type["set"])


            if cnts_types["count"] > (cnts_types["argmin"]+cnts_types['argmax'])*1.5:
                complex_retain.extend(random.sample(by_type["count"], k=min(len(by_type["count"]), math.floor((cnts_types["argmin"]+cnts_types['argmax'])*1.5))))
            else:
                complex_retain.extend(by_type["count"])


            retain_by_idx = defaultdict(list)

            for idx, item in complex_retain:
                retain_by_idx[idx].append(item)

            with open(file) as f, open(file+"_fix2","w+") as of:
                by_type = defaultdict(list)
                for idx, line in enumerate(f):
                    instance = json.loads(line)

                    new_queries = []
                    for q in instance["queries"]:
                        if q["type"] not in {"set","count","bool"}:
                            new_queries.append(q)

                    new_queries.extend(retain_by_idx[idx])
                    random.shuffle(new_queries)
                    instance["queries"] = new_queries

                    of.write(json.dumps(instance)+"\n")


        if "fix3" not in file:
            complex_retain = []

            for k in cnts_types.keys():
                if "complex" in k:
                    if cnts_types[k]>cnts_types[k.split("_complex")[0]] * .6:
                        complex_retain.extend(random.sample(by_type[k], k=min(len(by_type[k]), math.floor(cnts_types[k.split("_complex")[0]]*.6))))
                    else:
                        complex_retain.extend(by_type[k])

            retain_by_idx = defaultdict(list)

            for idx, item in complex_retain:
                retain_by_idx[idx].append(item)

            with open(file) as f, open(file+"_fix3","w+") as of:
                by_type = defaultdict(list)
                for idx, line in enumerate(f):
                    instance = json.loads(line)

                    new_queries = []
                    for q in instance["queries"]:
                        if "complex" not in q["type"]:
                            new_queries.append(q)

                    new_queries.extend(retain_by_idx[idx])
                    random.shuffle(new_queries)
                    instance["queries"] = new_queries

                    of.write(json.dumps(instance)+"\n")


        print(file)
        print(lct,qct,qct/lct)
        print(cnts_types)
        print(cnts)

        print()

