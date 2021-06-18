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
from operator import itemgetter
from torch.utils.data import Dataset
from tqdm import tqdm
import logging

logger = logging.getLogger(__name__)


class Seq2SeqDataset(Dataset):
    def __init__(self, generator, auto_pad=None):
        self.generator = generator
        self.auto_pad = auto_pad

        if self.auto_pad:
            self.features = list(
                map(
                    self.auto_pad,
                    tqdm(generator, desc="Reading and padding instances"),
                )
            )
        else:
            self.features = list(tqdm(generator, desc="Reading instances"))

    def __len__(self):
        return len(self.features)

    def __getitem__(self, item):
        return self.features[item]

    def to_dict(self):
        assert len(self.features)
        keys = self.features[0].keys()
        return {key: list(map(itemgetter(key), self.features)) for key in keys}
