import argparse
import glob
import logging
import os
import time

import torch
from similarity.normalized_levenshtein import NormalizedLevenshtein
from torch.utils.data import DataLoader
from transformers import get_linear_schedule_with_warmup

from log_helper import setup_logging
from transformer_base import BaseTransformer, add_generic_args, generic_train
from utils import NDBDataset, seq2seq_to_NDB

logger = logging.getLogger(__name__)



class Seq2seqTrainer(BaseTransformer):

    def __init__(self, hparams):
        super().__init__(hparams, num_labels=None)
        self.em = 0
        self.data_dir = self.hparams.data_dir
        self.source_length = self.hparams.max_source_length
        self.target_length = self.hparams.max_target_length
        self.output_dir = self.hparams.output_dir

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

        special_tokens = []

        for i in range(0, 101):
            special_tokens.append('<extra_id_' + str(i) + '>')

        special_tokens.extend(['[SEP]', 'NDB:'])  #
        self.tokenizer.add_special_tokens(
            {'additional_special_tokens': special_tokens})

        self.classes = ["<Yes>", "<No>", "<None>"]

        self.tokenizer.add_tokens(self.classes)

        self.model.resize_token_embeddings(len(self.tokenizer))

        self.bad_words = [[self.tokenizer.convert_tokens_to_ids(bad_word)] for bad_word in
                          self.tokenizer.additional_special_tokens]

    def forward(self, input_ids, attention_mask=None, decoder_input_ids=None, lm_labels=None):
        if decoder_input_ids == None:
            return self.model(
                input_ids, attention_mask=attention_mask, lm_labels=lm_labels,
            )
        else:
            return self.model(
                input_ids, attention_mask=attention_mask, decoder_input_ids=decoder_input_ids, lm_labels=lm_labels,
            )

    def _step(self, batch):
        pad_token_id = self.tokenizer.pad_token_id
        source_ids, source_mask, y = batch["source_ids"], batch["source_mask"], batch["target_ids"]

        if 'bart' in self.hparams.model_name_or_path:
            y_ids = y[:, :-1].contiguous()
            lm_labels = y[:, 1:].clone()
            lm_labels[y[:, 1:] == pad_token_id] = -100
            outputs = self(source_ids, attention_mask=source_mask, decoder_input_ids=y_ids, lm_labels=lm_labels, )

        if 't5' in self.hparams.model_name_or_path:
            lm_labels = y.clone()
            lm_labels[y == pad_token_id] = -100
            outputs = self(source_ids, attention_mask=source_mask, lm_labels=lm_labels, )

        loss = outputs[0]

        return loss

    def training_step(self, batch, batch_idx):
        loss = self._step(batch)

        tensorboard_logs = {"train_loss": loss}
        return {"loss": loss, "log": tensorboard_logs}

    def validation_step(self, batch, batch_idx):
        pad_token_id = self.tokenizer.pad_token_id

        ids, source_ids, source_mask, y = NDBDataset.trim_seq2seq_batch(batch, pad_token_id)
        generated_ids = self.model.generate(
            input_ids=source_ids,
            attention_mask=source_mask,
            num_beams=1,
            max_length=self.target_length,
            repetition_penalty=1,
            length_penalty=1.0,
            early_stopping=True,
            use_cache=True,
            do_sample=False,
            top_p=0.95,
            top_k=50,
            bad_words_ids=self.bad_words
        )

        preds = [self.tokenizer.decode(g, skip_special_tokens=True) for g in generated_ids]
        target = [self.tokenizer.decode(t, skip_special_tokens=True) for t in y]
        loss = self._step(batch)
        sources = [self.tokenizer.decode(s) for s in source_ids]

        return {"val_loss": loss, 'id': ids, 'sources': sources, "preds": preds, "targets": target}

    def validation_end(self, outputs):
        normalized_levenshtein = NormalizedLevenshtein()
        avg_loss = torch.stack([x["val_loss"] for x in outputs]).mean()
        tensorboard_logs = {"val_loss": avg_loss}

        preds = []
        targets = []
        sources = []
        ids = []
        for batch in outputs:
            sources.extend(batch['sources'])
            targets.extend(batch['targets'])
            preds.extend(batch['preds'])
            ids.extend(batch['id'])

        em = 0.0
        for s, pred, t in zip(sources, preds, targets):
            pred = pred.strip()
            t = t.strip()
            # print(s)
            # print(pred +' : '+t)
            if t in self.classes:

                if pred == t:
                    em = em + 1.0
            else:

                em = em + normalized_levenshtein.similarity(pred, t)

        if float(em) / len(preds) > self.em:
            self.em = float(em) / len(preds)
            self.trainer.save_checkpoint(self.output_dir + '/' + "best_em.ckpt")
            seq2seq_to_NDB(ids, sources, preds, self.hparams.output_dir, 'dev')
        return {"avg_val_loss": avg_loss, "log": tensorboard_logs, "EM": float(em) / len(preds)}

    def test_step(self, batch, batch_idx):
        pad_token_id = self.tokenizer.pad_token_id

        ids, source_ids, source_mask, y = NDBDataset.trim_seq2seq_batch(batch, pad_token_id)
        # NOTE: the following kwargs get more speed and lower quality summaries than those in evaluate_kilt_task.py

        generated_ids = self.model.generate(
            input_ids=source_ids,
            attention_mask=source_mask,
            num_beams=1,
            max_length=self.target_length,
            repetition_penalty=1,
            length_penalty=1.0,
            early_stopping=True,
            use_cache=True,
            do_sample=False,
            top_p=0.95,
            top_k=50,
            bad_words_ids=self.bad_words
        )
        preds = [self.tokenizer.decode(g) for g in generated_ids]
        target = [self.tokenizer.decode(t) for t in y]
        loss = self._step(batch)
        sources = [self.tokenizer.decode(s) for s in source_ids]
        return {"val_loss": loss, 'id': ids, 'sources': sources, "preds": preds, "target": target}

    def test_epoch_end(self, outputs):
        avg_loss = torch.stack([x["val_loss"] for x in outputs]).mean()
        tensorboard_logs = {"val_loss": avg_loss}
        return {"avg_val_loss": avg_loss, "log": tensorboard_logs}

    def test_end(self, outputs):
        sources = []
        preds = []
        ids = []
        for batch in outputs:
            sources.extend(batch['sources'])
            preds.extend(batch['preds'])
            ids.extend(batch['id'])

        seq2seq_to_NDB(ids, sources, preds, self.hparams.output_dir, 'test')

        return self.test_epoch_end(outputs)

    def get_dataloader(self, type_path: str, batch_size: int, shuffle: bool = False) -> DataLoader:

        percentage = self.hparams.train_percentage if type_path == 'train' else self.hparams.dev_percentage
        dataset = NDBDataset(self.tokenizer, type_path=type_path, max_source_length=self.source_length,
                             max_target_length=self.target_length, data_dir=self.data_dir, percentage=percentage)
        dataloader = DataLoader(dataset, batch_size=batch_size, collate_fn=dataset.collate_fn, shuffle=shuffle)
        return dataloader

    def train_dataloader(self) -> DataLoader:
        dataloader = self.get_dataloader("train_queries_last_50", batch_size=self.hparams.train_batch_size, shuffle=True)
        t_total = (
                (len(dataloader.dataset) // (self.hparams.train_batch_size * max(1, self.hparams.n_gpu)))
                // self.hparams.gradient_accumulation_steps
                * float(self.hparams.num_train_epochs)
        )
        scheduler = get_linear_schedule_with_warmup(
            self.opt, num_warmup_steps=self.hparams.warmup_steps, num_training_steps=t_total
        )
        self.lr_scheduler = scheduler
        return dataloader

    def val_dataloader(self) -> DataLoader:
        return self.get_dataloader("dev_queries_last_50", batch_size=self.hparams.eval_batch_size)

    def test_dataloader(self) -> DataLoader:
        return self.get_dataloader("test_queries_last_50", batch_size=self.hparams.eval_batch_size)

    @staticmethod
    def add_model_specific_args(parser, root_dir):
        BaseTransformer.add_model_specific_args(parser, root_dir)

        parser.add_argument(
            "--max_source_length",
            default=256,
            type=int,
            help="The maximum total input sequence length after tokenization. Sequences longer "
                 "than this will be truncated, sequences shorter will be padded.",
        )
        parser.add_argument(
            "--max_target_length",
            default=10,
            type=int,
            help="The maximum total input sequence length after tokenization. Sequences longer "
                 "than this will be truncated, sequences shorter will be padded.",
        )

        parser.add_argument(
            "--data_dir",
            default=None,
            type=str,
            required=True,
            help="The input data dir. Should contain the dataset files for the task.",
        )
        return parser


def main(args):
    # If output_dir not provided, a folder will be generated in pwd
    if not args.output_dir:
        args.output_dir = os.path.join("./results", f"{args.task}_{time.strftime('%Y%m%d_%H%M%S')}", )
        os.makedirs(args.output_dir)
    model = Seq2seqTrainer(args)
    trainer = generic_train(model, args)

    # Optionally, predict on dev set and write to output_dir
    if args.do_predict:
        checkpoints = list(sorted(glob.glob(os.path.join(args.output_dir, "checkpointepoch=*.ckpt"), recursive=True)))
        model = model.load_from_checkpoint(checkpoints[-1])
        trainer.test(model)


if __name__ == "__main__":
    setup_logging()
    parser = argparse.ArgumentParser()
    add_generic_args(parser)
    parser = Seq2seqTrainer.add_model_specific_args(parser, os.getcwd())
    args = parser.parse_args()

    main(args)
