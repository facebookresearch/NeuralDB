import json
from collections import defaultdict

if __name__ == "__main__":
    by_db_qid = defaultdict(dict)
    with open("resources/v1.8_2500_sup/dev_0.76_st_ssg_ds.json") as f:
        loaded = json.load(f)
        for item in loaded:
            by_db_qid[item["db_id"]][item["question_id"]] = item

    with open("resources/v1.8_2500/dev.jsonl") as f, open("resources/v1.8_2500/dev_ssg.jsonl","w+") as of:
        for db_id, line in enumerate(f):
            db = json.loads(line)

            for idx,query in enumerate(db["queries"]):
                found = by_db_qid[db_id][idx]
                ssg = []
                for group in found["ssg_output"]:
                    grp = []
                    for fact_id, fact_sent in group:
                       grp.append(fact_id)
                    ssg.append(grp)
                query["predicted_facts"] = ssg

            of.write(json.dumps(db)+"\n")

