import json
import os

import torch
from torch.utils.data import Dataset
from transformers import T5Tokenizer, BartTokenizer
from transformers.tokenization_utils import trim_batch


def NDB_to_seq2seq(data_dir, type_path, sep_token, p):
    data_file = os.path.join(data_dir, type_path + ".json")

    sources = []
    targets = []
    ids = []

    with open(data_file) as json_file:
        data = json.load(json_file)
    counter = 0
    q_counter = 0
    limit = p * len(data)
    for d in data:
        if counter > limit:
            break
        counter = counter + 1
        updates = [u[1] for u in d['updates']]
        questions = d['queries']
        for q in questions:
            t = int(q[0])
            question = q[1]
            q_counter += 1
            answer = q[2]
            source_string = question
            if 'None' in answer:
                context = updates[0:t]
            else:
                context = updates
            context.reverse()
            for u in context:
                source_string += " " + sep_token + " " + u

            sources.append(source_string.strip())
            targets.append(answer.strip())
            ids.append(q_counter)

    return ids, sources, targets


def encode_seq(tokenizer, seqs, max_length, out_dir, side='source', type_path='train', pad_to_max_length=True,
               return_tensors="pt"):
    examples = []

    output_file = os.path.join(out_dir, type_path + "-" + side + ".encoded")
    with open(output_file, "w") as f_out:
        for text in seqs:

            if side == 'target':
                if text == "Yes":
                    text = "<Yes>"
                if text == "No":
                    text = "<No>"
                if text == "None":
                    text = "<None>"

            txt = text if side == 'target' else \
                "NDB: " + text
            txt = txt + tokenizer.eos_token
            tokenized = tokenizer.batch_encode_plus(
                [txt], add_special_tokens=True, max_length=max_length, pad_to_max_length=pad_to_max_length,
                return_tensors=return_tensors,
            )

            tokens = tokenizer.convert_ids_to_tokens(tokenized["input_ids"][0])
            f_out.write(' | '.join(tokens) + "\n")
            examples.append(tokenized)

    return examples


class NDBDataset(Dataset):
    def __init__(
            self,
            tokenizer,
            data_dir="./v0/",
            type_path="train",
            max_source_length=256,
            max_target_length=10,
            percentage=1
    ):
        super().__init__()
        self.tokenizer = tokenizer
        self.sep = "[SEP]" if tokenizer.sep_token is None else tokenizer.sep_token
        self.ids, sources, targets = NDB_to_seq2seq(data_dir, type_path, self.sep, percentage)

        self.source = encode_seq(tokenizer, sources, max_source_length, data_dir, 'source', type_path)
        self.target = encode_seq(tokenizer, targets, max_target_length, data_dir, 'target', type_path)

    def __len__(self):
        return len(self.source)

    def __getitem__(self, index):
        id = self.ids[index]
        source_ids = self.source[index]["input_ids"].squeeze()
        target_ids = self.target[index]["input_ids"].squeeze()
        src_mask = self.source[index]["attention_mask"].squeeze()
        return {"id": id, "source_ids": source_ids, "source_mask": src_mask, "target_ids": target_ids}

    @staticmethod
    def trim_seq2seq_batch(batch, pad_token_id):
        y = trim_batch(batch["target_ids"], pad_token_id)
        source_ids, source_mask = trim_batch(batch["source_ids"], pad_token_id, attention_mask=batch["source_mask"])
        ids = batch["id"]
        return ids, source_ids, source_mask, y

    def collate_fn(self, batch):
        ids = [x["id"] for x in batch]
        input_ids = torch.stack([x["source_ids"] for x in batch])
        masks = torch.stack([x["source_mask"] for x in batch])
        target_ids = torch.stack([x["target_ids"] for x in batch])
        pad_token_id = self.tokenizer.pad_token_id
        y = trim_batch(target_ids, pad_token_id)
        source_ids, source_mask = trim_batch(input_ids, pad_token_id, attention_mask=masks)
        return {'id': ids, "source_ids": source_ids, "source_mask": source_mask, "target_ids": y}


def seq2seq_to_NDB(ids, sources, targets, output_dir, type_path):
    data_file = os.path.join(output_dir, type_path + ".json")
    qs = {'queries': [], 'id': []}
    with open(data_file, "w") as output_file:
        for q_id, s, t in zip(ids, sources, targets):
            t = t.strip()
            if t in ['<Yes>', '<No>', '<None>']:
                t = t.replace('<', '').replace('>', '')

            a = t

            qs['queries'].append(a)
            qs['id'].append(q_id)

        json.dump(qs, output_file)


if __name__ == "__main__":
    tokenizer_t5 = T5Tokenizer.from_pretrained('t5-base')
    tokenizer_bart = BartTokenizer.from_pretrained('bart-large')

    tokens = tokenizer_t5.encode_plus("Majid is cool , what's up", add_special_tokens=True)

    print(tokenizer_t5.convert_ids_to_tokens(tokens['input_ids']))
    print(tokenizer_t5.pad_token)
    print(tokenizer_t5.eos_token)
    print(tokenizer_t5.sep_token)
    tokens = tokenizer_bart.encode_plus("Majid is cool , what's up", add_special_tokens=True)
    print(tokenizer_bart.convert_ids_to_tokens(tokens['input_ids']))
    print(tokenizer_bart.pad_token)
    print(tokenizer_bart.eos_token)
    print(tokenizer_bart.sep_token)
    t = ''
    if t in ['<Yes>', '<No>', '<None>']:
        print(t)
    # NDB_to_seq2seq('../data/gen/v0', '../data/gen/v0', 'dev', '<>')
    # NDB_to_seq2seq('../data/gen/v0', '../data/gen/v0', 'train', '<>')
    # NDB_to_seq2seq('../data/gen/v0', '../data/gen/v0', 'test', '<>')
