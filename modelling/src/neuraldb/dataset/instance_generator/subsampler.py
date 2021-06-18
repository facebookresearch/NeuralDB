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
import random


class Subsampler:

    # Take a list of sample types and probability of keeping
    def __init__(self, sample_types):
        self.sample_types = sample_types

    #
    def maybe_drop_sample(self, query):
        if query["type"] in self.sample_types:
            sample_rate = self.sample_types[query["type"]]
            rand = random.random()

            if isinstance(sample_rate, list):
                if not len(query["answer"]):
                    sample_rate = sample_rate[2]
                else:
                    if "TRUE" in query["answer"]:
                        sample_rate = sample_rate[0]
                    else:
                        sample_rate = sample_rate[1]

            # Drop sample if needed
            return rand < sample_rate

        return False
