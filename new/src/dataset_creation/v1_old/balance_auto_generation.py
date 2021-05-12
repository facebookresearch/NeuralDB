import json
import random
import sys
from collections import Counter

if __name__ == "__main__":

    cut_rels = {'P54','P106','P21','P1082','P27','P19'}
    cut_rels2 = {'P69','P47'}
    counter_t = Counter()
    with open(sys.argv[1]) as f, open(sys.argv[2],"w+") as of:
        for line in f:
            instance = json.loads(line)
            if instance['entity_ids']['relation'] in cut_rels:
                if random.uniform(0,1) < 0.9:
                    continue
            if instance['entity_ids']['relation'] in cut_rels2:
                if random.uniform(0,1) < 0.75:
                    continue

            counter_t[instance['entity_ids']['relation']] += 1
            of.write(line)
    print(counter_t)

