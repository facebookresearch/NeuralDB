import torch
from torch.utils.data import Dataset
from tqdm import tqdm


class DeferredDataset(Dataset):
    def __init__(self, reader, generator):
        self.reader = reader
        self.generator = generator

    def __len__(self):
        return len(self.features)

    def __getitem__(self, item):
        return self.features[item]

    def read(self, path):
        train_data = self.reader.read(path)
        self.features = list(tqdm(train_data, desc="Reading training instances"))
