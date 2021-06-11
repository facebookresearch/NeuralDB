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
