import numpy as np
import linecache
import random
import sys
from copy import copy
import torch
from torch.utils.data import Dataset, Sampler
from tqdm import tqdm
from typing import Dict, Callable, Iterable, List
from pathlib import Path
from transformers import BartTokenizer


def encode_line(tokenizer, line, max_length, pad_to_max_length=True, return_tensors="pt"):
    extra_kw = {"add_prefix_space": True} if isinstance(tokenizer, BartTokenizer) else {}
    return tokenizer(
        [line],
        max_length=max_length,
        padding="max_length" if pad_to_max_length else None,
        truncation=True,
        return_tensors=return_tensors,
        **extra_kw,
    )


def lmap(f: Callable, x: Iterable) -> List:
    """list(map(f, x))"""
    return list(map(f, x))


def trim_batch(
    input_ids, pad_token_id, attention_mask=None,
):
    """Remove columns that are populated exclusively by pad_token_id"""
    keep_column_mask = input_ids.ne(pad_token_id).any(dim=0)
    if attention_mask is None:
        return input_ids[:, keep_column_mask]
    else:
        return (input_ids[:, keep_column_mask], attention_mask[:, keep_column_mask])



class SortishSampler(Sampler):
    "Go through the text data by order of src length with a bit of randomness. From fastai repo."

    def __init__(self, data, batch_size):
        self.data, self.bs = data, batch_size

    def key(self, i):
        return self.data[i]

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self):
        idxs = np.random.permutation(len(self.data))
        sz = self.bs * 50
        ck_idx = [idxs[i : i + sz] for i in range(0, len(idxs), sz)]
        sort_idx = np.concatenate([sorted(s, key=self.key, reverse=True) for s in ck_idx])
        sz = self.bs
        ck_idx = [sort_idx[i : i + sz] for i in range(0, len(sort_idx), sz)]
        max_ck = np.argmax([self.key(ck[0]) for ck in ck_idx])  # find the chunk with the largest key,
        ck_idx[0], ck_idx[max_ck] = ck_idx[max_ck], ck_idx[0]  # then make sure it goes first.
        sort_idx = np.concatenate(np.random.permutation(ck_idx[1:])) if len(ck_idx) > 1 else np.array([], dtype=np.int)
        sort_idx = np.concatenate((ck_idx[0], sort_idx))
        return iter(sort_idx)



def recursive_clean(metadata_dict):
    return {k: (recursive_clean(v) if "items" in dir(v) else v) for k, v in metadata_dict.items() if v is not None}


class GenericDataset(Dataset):

    def __init__(
            self,
            tokenizer,
            instance_generator,
            max_source_length,
            max_target_length,
    ):
        super().__init__()
        self.instances = list(tqdm(filter(lambda i: i is not None, instance_generator)))

        self.max_source_length = max_source_length
        self.max_target_length = max_target_length
        self.tokenizer = tokenizer
        self.pad_token_id = self.tokenizer.pad_token_id
        self.has_preview = 0
        self.labels = dict()
        self.tokenizer.add_special_tokens({"additional_special_tokens":instance_generator.special_tokens})

    def __len__(self):
        return len(self.instances)

    def __getitem__(self, index) -> Dict[str, torch.Tensor]:
        instance = self.instances[index]
        return instance
        # source_inputs = encode_line(self.tokenizer, instance["source"], self.max_source_length)
        # target_inputs = encode_line(self.tokenizer, instance["target"]  + " </s>", self.max_target_length)
        #
        # source_ids = source_inputs["input_ids"].squeeze()
        # target_ids = target_inputs["input_ids"].squeeze()
        # src_mask = source_inputs["attention_mask"].squeeze()
        #
        # if self.has_preview<5:
        #     self.has_preview += 1
        #     print(source_inputs)
        #     print(target_inputs)
        #     print(target_ids)
        #     print(recursive_clean({k: v for k, v in instance.items() if v is not None}))
        #     print("*"*100)
        #
        # return {
        #     "input_ids": source_ids,
        #     "attention_mask": src_mask,
        #     "decoder_input_ids": target_ids,
        #     "metadata": recursive_clean({k:v for k,v in instance.items() if v is not None})
        # }

    @staticmethod
    def get_char_lens(data_file):
        return [len(x) for x in Path(data_file).open().readlines()]

    @staticmethod
    def trim_seq2seq_batch(batch, pad_token_id) -> tuple:
        y = trim_batch(batch["decoder_input_ids"], pad_token_id)
        source_ids, source_mask = trim_batch(batch["input_ids"], pad_token_id, attention_mask=batch["attention_mask"])
        return source_ids, source_mask, y

    def collate_fn(self, batch) -> Dict[str, torch.Tensor]:
        input_ids = torch.stack([x["input_ids"] for x in batch])
        masks = torch.stack([x["attention_mask"] for x in batch])
        target_ids = torch.stack([x["decoder_input_ids"] for x in batch])
        pad_token_id = self.pad_token_id
        y = trim_batch(target_ids, pad_token_id)
        source_ids, source_mask = trim_batch(input_ids, pad_token_id, attention_mask=masks)
        batch = {
            "input_ids": source_ids,
            "attention_mask": source_mask,
            "decoder_input_ids": y,
            "labels": y,
            #"metadata": [x["metadata"] for x in batch if x is not None]
        }

        return batch

    def make_sortish_sampler(self, batch_size):
        return SortishSampler(self.src_lens, batch_size)