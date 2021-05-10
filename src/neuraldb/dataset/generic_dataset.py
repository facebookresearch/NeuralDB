import math
import torch
from torch.utils.data import Dataset, IterableDataset
from tqdm import tqdm
import random


class GenericDataset(Dataset):
    def __init__(self, reader, generator, auto_pad=True, percentage=None):
        self.reader = reader
        self.generator = generator
        self.auto_pad = auto_pad
        self.percentage = percentage

    def __len__(self):
        return len(self.features)

    def __getitem__(self, item):
        return self.features[item]

    def read(self, path):
        train_data = self.reader.read(path)

        if self.auto_pad:
            self.features = list(
                map(
                    self.generator.pad,
                    tqdm(train_data, desc="Reading instance from {}".format(path)),
                )
            )
        else:
            self.features = list(
                tqdm(train_data, desc="Reading instance from {}".format(path))
            )

        if (
            "test" not in path
            and "val" not in path
            and "dev" not in path
            and self.percentage is not None
        ):
            print("Sampling subset of data")
            self.features = random.sample(
                self.features, k=math.ceil(self.percentage * len(self.features))
            )


class AutoLoadDataset(IterableDataset):
    def __init__(self, reader, generator, auto_pad=True, percentage=None):
        self.reader = reader
        self.generator = generator
        self.auto_pad = auto_pad
        self.percentage = percentage

    def __iter__(self):
        yield from self.reader.read(self.path)

    def read(self, path):
        self.path = path

    def __len__(self):
        return 500
