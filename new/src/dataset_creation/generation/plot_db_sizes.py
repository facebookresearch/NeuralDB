import json
from operator import itemgetter

import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":


    with open("db_sizes.jsonl") as f:
        plot = []

        for line in f:
            db = json.loads(line)
            size = int(db["file"].split(".")[0].rsplit("_",maxsplit=1)[1])
            l5,lq,med,uq,u95,highest = np.percentile(db["sizes"],(1,25,50,75,99,100))

            plot.append((size,(l5,lq,med,uq,u95,highest)))

        plot.sort(key=itemgetter(0))
    lowers5 = [p[0] for q,p in plot]
    lowers = [p[1] for q,p in plot]
    median = [p[2] for q,p in plot]
    uppers = [p[3] for q,p in plot]
    upper5 = [p[4] for q,p in plot]
    limit = [p[5] for q,p in plot]
    nums = [q for q,p in plot]

    plt.fill_between(nums,lowers,uppers,alpha=0.3,color="purple")
    plt.fill_between(nums,lowers5,upper5,alpha=0.3,color="blue")
    plt.plot(nums,median,color="blue")
    plt.plot(nums,limit,color="blue")
    plt.title("KELM Database size")
    plt.ylabel("Number of subword tokens (T5 tokenizer)")
    plt.xlabel("Number of facts")
    plt.hlines(1024,0,50)

    plt.legend(["Median","Max","25th Percentile", "99th percentile", "Budget"])

    plt.show()