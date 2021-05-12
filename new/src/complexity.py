import json
import numpy as np
from collections import Counter
from nltk import word_tokenize
from matplotlib import pyplot as plt
from tqdm import tqdm

if __name__ == "__main__":
    query_lengths = []
    fact_lengths = []
    new_fact_lengths = []

    all_query_toks = Counter()
    all_fact_toks = Counter()

    with open('../../NeuralDB/generated_clean_val.jsonl') as f:
        for idx, line in enumerate(tqdm(f)):
            instance = json.loads(line)

            query_toks = word_tokenize(instance["query"].lower())
            fact_toks = word_tokenize(instance["fact"].lower())

            query_lengths.append(len(query_toks))
            fact_lengths.append(len(fact_toks))

            all_query_toks.update(query_toks)
            all_fact_toks.update(fact_toks)

            if idx > 5e5:
                break

    new_fact_toks = Counter()
    with open("../resources/out_aaa") as f:
        for idx, line in enumerate(tqdm(f)):
            instance = json.loads(line)
            fact_toks = word_tokenize(instance["candidate"].strip().lower())

            new_fact_lengths.append(len(fact_toks))
            new_fact_toks.update(fact_toks)

            if idx > 5e5:
                break

    a = list(all_fact_toks.values())
    b = list(new_fact_toks.values())

    a.sort(reverse=True)
    b.sort(reverse=True)
    plt.plot(a[:2000000])
    plt.plot(b[:2000000])
    plt.xscale("log")
    plt.yscale("log")
    plt.title("Token distribution")
    plt.xlabel("(log scale) token rank")
    plt.ylabel("(log scale) token count")

    plt.legend(["Template NDB","KELM"])
    plt.savefig("tst.png")
    plt.close()

    h1 = np.array(new_fact_lengths)
    h2 = np.array(fact_lengths)

    percs = np.percentile(h1,range(10,100,10))
    percs2 = np.percentile(h2,range(10,100,10))

    plt.hist(h2, bins=percs2, alpha=0.5, color="blue")
    plt.hist(h1, bins=percs, alpha=0.5, color="red")
    plt.title("histogram")
    plt.xlabel("Fact length (decile bins)")
    plt.ylabel("Count")
    plt.legend(["Template NDB","KELM"])
    plt.savefig("tdt.png")

    print(np.mean(new_fact_lengths), np.mean(fact_lengths))