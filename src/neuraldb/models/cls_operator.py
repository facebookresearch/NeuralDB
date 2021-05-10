import argparse
import glob
import logging
import os
import time

import numpy as np
import torch
from sklearn.metrics import f1_score
from torch.utils.data import DataLoader
from transformers.data.metrics import simple_accuracy

from lightning_base import BaseTransformer, add_generic_args, generic_train
from transformers import (
    glue_compute_metrics as compute_metrics,
    get_linear_schedule_with_warmup,
)
from transformers import (
    glue_convert_examples_to_features as convert_examples_to_features,
)
from transformers import glue_output_modes
from transformers import glue_processors as processors
from transformers import glue_tasks_num_labels

from neuraldb.dataset.generic_dataset import GenericDataset
from neuraldb.dataset.nuo_generator.nuo_op_classifier_generator import (
    NUOClassifierGenerator,
)
from neuraldb.dataset.unary_operator_reader import UnaryOperatorReader

logger = logging.getLogger(__name__)


class CLSTransformer(BaseTransformer):

    mode = "sequence-classification"

    def __init__(self, hparams):
        num_labels = 7
        super().__init__(hparams, num_labels, self.mode)

        self.source_length = self.hparams.max_seq_length
        self.data_generator = self.construct_generator()
        self.reader = UnaryOperatorReader(self.data_generator)
        self.model.resize_token_embeddings(len(self.tokenizer))

    def construct_generator(self):
        return NUOClassifierGenerator(
            self.tokenizer,
            context_limit=self.source_length,
            test_mode=hasattr(self.hparams, "external_test"),
        )

    def forward(self, **inputs):
        return self.model(**inputs)

    def training_step(self, batch, batch_idx):
        inputs = {
            "input_ids": batch["input_ids"],
            "attention_mask": batch["attention_mask"],
            "labels": batch["labels"],
        }

        outputs = self(**inputs)
        loss = outputs[0]
        self.trainer.total_loss = getattr(self.trainer, "total_loss", 0.0) + loss
        self.trainer.avg_loss = loss
        tensorboard_logs = {"loss": loss, "rate": self.lr_scheduler.get_last_lr()[-1]}
        return {"loss": loss, "log": tensorboard_logs}

    def get_dataloader(
        self, type_path: str, batch_size: int, shuffle: bool = False, percentage=None
    ) -> DataLoader:
        ds = GenericDataset(
            self.reader, self.data_generator, auto_pad=False, percentage=percentage
        )
        ds.read(type_path)
        data_loader = DataLoader(
            ds,
            batch_size=batch_size,
            collate_fn=self.data_generator.collate_fn,
            shuffle=shuffle,
        )
        return data_loader

    def train_dataloader(self) -> DataLoader:
        dataloader = self.get_dataloader(
            self.hparams.train_path,
            batch_size=self.hparams.train_batch_size,
            shuffle=True,
            percentage=1.0,
        )
        t_total = (
            (
                len(dataloader.dataset)
                // (self.hparams.train_batch_size * max(1, self.hparams.n_gpu))
            )
            // self.hparams.gradient_accumulation_steps
            * float(self.hparams.num_train_epochs)
        )
        scheduler = get_linear_schedule_with_warmup(
            self.opt,
            num_warmup_steps=self.hparams.warmup_steps,
            num_training_steps=t_total,
        )
        self.lr_scheduler = scheduler
        return dataloader

    def val_dataloader(self) -> DataLoader:
        return self.get_dataloader(
            self.hparams.val_path, batch_size=self.hparams.eval_batch_size
        )

    def test_dataloader(self) -> DataLoader:
        return self.get_dataloader(
            self.hparams.test_path, batch_size=self.hparams.eval_batch_size
        )

    def validation_step(self, batch, batch_idx):
        inputs = {
            "input_ids": batch["input_ids"],
            "attention_mask": batch["attention_mask"],
            "labels": batch["labels"],
        }

        outputs = self(**inputs)
        tmp_eval_loss, logits = outputs[:2]
        preds = logits.detach().cpu().numpy()
        out_label_ids = inputs["labels"].detach().cpu().numpy()
        self.trainer.total_loss = (
            getattr(self.trainer, "total_loss", 0.0) + tmp_eval_loss
        )
        self.trainer.avg_loss = tmp_eval_loss

        return {
            "val_loss": tmp_eval_loss.detach().cpu(),
            "pred": preds,
            "target": out_label_ids,
        }

    def test_step(self, batch, batch_idx):
        return self.validation_step(batch, batch_idx)

    @staticmethod
    def acc_and_f1(preds, labels):
        acc = simple_accuracy(preds, labels)
        f1 = f1_score(y_true=labels, y_pred=preds, average="macro")
        return {
            "acc": acc,
            "f1": f1,
            "acc_and_f1": (acc + f1) / 2,
        }

    @staticmethod
    def compute_metrics(preds, labels):
        assert len(preds) == len(labels)
        return CLSTransformer.acc_and_f1(preds, labels)

    def _eval_end(self, outputs):
        val_loss_mean = (
            torch.stack([x["val_loss"] for x in outputs]).mean().detach().cpu().item()
        )
        preds = np.concatenate([x["pred"] for x in outputs], axis=0)
        preds = np.argmax(preds, axis=1)

        out_label_ids = np.concatenate([x["target"] for x in outputs], axis=0)
        out_label_list = [[] for _ in range(out_label_ids.shape[0])]
        preds_list = [[] for _ in range(out_label_ids.shape[0])]

        results = {
            **{"val_loss": val_loss_mean},
            **self.compute_metrics(preds, out_label_ids),
        }

        ret = {k: v for k, v in results.items()}
        ret["log"] = results
        return ret, preds_list, out_label_list

    def validation_epoch_end(self, outputs: list) -> dict:
        ret, preds, targets = self._eval_end(outputs)
        logs = ret["log"]
        return {"val_loss": logs["val_loss"], "log": logs, "progress_bar": logs}

    def test_epoch_end(self, outputs):
        # updating to test_epoch_end instead of deprecated test_end
        ret, predictions, targets = self._eval_end(outputs)

        # Converting to the dic required by pl
        # https://github.com/PyTorchLightning/pytorch-lightning/blob/master/\
        # pytorch_lightning/trainer/logging.py#L139
        logs = ret["log"]
        # `val_loss` is the key returned by `self._eval_end()` but actually refers to `test_loss`
        return {"avg_test_loss": logs["val_loss"], "log": logs, "progress_bar": logs}

    @staticmethod
    def add_model_specific_args(parser, root_dir):
        # Add NER specific options
        BaseTransformer.add_model_specific_args(parser, root_dir)
        parser.add_argument(
            "--max_seq_length",
            default=128,
            type=int,
            help="The maximum total input sequence length after tokenization. Sequences longer "
            "than this will be truncated, sequences shorter will be padded.",
        )

        parser.add_argument(
            "--train_path", type=str, required=True, help="Path to training data file"
        )

        parser.add_argument(
            "--val_path", type=str, required=True, help="Path to validation data file"
        )

        parser.add_argument(
            "--test_path", type=str, required=False, help="Path to test data file"
        )

        return parser
