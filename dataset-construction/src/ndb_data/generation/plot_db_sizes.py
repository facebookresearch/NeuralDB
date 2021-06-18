#
# Copyright (c) 2021 Facebook, Inc. and its affiliates.
#
# This file is part of NeuralDB.
# See https://github.com/facebookresearch/NeuralDB for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import json
from operator import itemgetter

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    with open("db_sizes.jsonl") as f:
        plot = []

        for line in f:
            db = json.loads(line)
            size = int(db["file"].split(".")[0].rsplit("_", maxsplit=1)[1])
            l5, lq, med, uq, u95, highest = np.percentile(
                db["sizes"], (1, 25, 50, 75, 99, 100)
            )

            plot.append((size, (l5, lq, med, uq, u95, highest)))

        plot.sort(key=itemgetter(0))
    lowers5 = [p[0] for q, p in plot]
    lowers = [p[1] for q, p in plot]
    median = [p[2] for q, p in plot]
    uppers = [p[3] for q, p in plot]
    upper5 = [p[4] for q, p in plot]
    limit = [p[5] for q, p in plot]
    nums = [q for q, p in plot]

    plt.fill_between(nums, lowers, uppers, alpha=0.3, color="purple")
    plt.fill_between(nums, lowers5, upper5, alpha=0.3, color="blue")
    plt.plot(nums, median, color="blue")
    plt.plot(nums, limit, color="blue")
    plt.title("KELM Database size")
    plt.ylabel("Number of subword tokens (T5 tokenizer)")
    plt.xlabel("Number of facts")
    plt.hlines(1024, 0, 50)

    plt.legend(["Median", "Max", "25th Percentile", "99th percentile", "Budget"])

    plt.show()
