import argparse
import glob
import logging
import os
import time

import numpy as np
import torch
from torch.utils.data import DataLoader, TensorDataset

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

from neuraldb.dataset.base_reader import (
    NeuralDatabaseDatasetReader,
    NeuralDatabaseDatasetShuffleReader,
)
from neuraldb.dataset.e2e_generator.seq2seq_reader import Seq2SeqSpecificGenerator
from neuraldb.dataset.e2e_generator.surrogate_test import (
    Seq2SeqSpecificSurrogateGenerator,
)
from neuraldb.dataset.e2e_reader.v0_5_database_reader import V5DatabaseSpecificReader
from neuraldb.dataset.generic_dataset import GenericDataset, AutoLoadDataset
from neuraldb.dataset.search_engines.return_all import ReturnAll
from neuraldb.models.seq2seqargs import Seq2seqTrainer

logger = logging.getLogger(__name__)


class GLUETransformer(BaseTransformer):

    mode = "sequence-classification"

    def __init__(self, hparams):
        hparams.glue_output_mode = "classification"
        num_labels = 2
        super().__init__(hparams, num_labels, self.mode)

        self.surrogate = Seq2seqTrainer.load_from_checkpoint(
            hparams.surrogate + "/best_em.ckpt"
        )
        self.surrogate.data_generator.test_mode = True

        self.data_reader = self.get_dataset_reader()
        self.data_generator = self.construct_generator()
        self.reader = NeuralDatabaseDatasetShuffleReader(
            self.data_reader, self.data_generator
        )

        self.predicted_labels, self.gold_labels = [], []

    def forward(self, **inputs):
        return self.model(**inputs)

    def training_step(self, batch, batch_idx):

        inputs = {"input_ids": batch[0], "attention_mask": batch[1], "labels": batch[2]}
        outputs = self(**inputs)
        loss = outputs[0]
        self.predicted_labels.extend(
            torch.argmax(outputs[1], dim=1).cpu().detach().numpy().tolist()
        )
        self.gold_labels.extend(batch[2].cpu().numpy().tolist())
        self.predicted_labels, self.gold_labels = (
            self.predicted_labels[-1000:],
            self.gold_labels[-1000:],
        )
        self.trainer.avg_loss = loss.item()
        tqdm_dict = compute_metrics(
            "mrpc", np.array(self.predicted_labels), np.array(self.gold_labels)
        )

        # preds = np.concatenate([x["pred"] for x in outputs], axis=0)
        #
        # if self.hparams.glue_output_mode == "classification":
        #     preds = np.argmax(preds, axis=1)
        # elif self.hparams.glue_output_mode == "regression":
        #     preds = np.squeeze(preds)
        #
        # out_label_ids = np.concatenate([x["target"] for x in outputs], axis=0)
        # out_label_list = [[] for _ in range(out_label_ids.shape[0])]
        # preds_list = [[] for _ in range(out_label_ids.shape[0])]
        #
        # results = {**{"val_loss": val_loss_mean}, **compute_metrics("mnli", preds, out_label_ids)}
        #
        # for output in outputs:
        #     val_acc_mean += output['val_acc']
        #
        # val_acc_mean /= len(outputs)
        # tqdm_dict = {'val_acc': val_acc_mean.item()}
        #
        # # show val_acc in progress bar but only log val_loss
        # results = {
        #     'progress_bar': tqdm_dict,
        #     'log': {'val_acc': val_acc_mean.item()}
        # }
        # return results

        tensorboard_logs = {
            "loss": loss,
            "rate": self.lr_scheduler.get_last_lr()[-1],
            **tqdm_dict,
        }
        return {"loss": loss, "log": tensorboard_logs, "progress_bar": tqdm_dict}

    def get_dataset_reader(self):
        return V5DatabaseSpecificReader(
            max_queries=None, max_list_len=None, filter_types=None
        )

    def construct_generator(self):
        def fwd(instances):

            loader = DataLoader(
                [self.surrogate.data_generator.pad(i) for i in instances],
                batch_size=32,
                collate_fn=self.surrogate.data_generator.collate_fn,
            )

            projected = []
            with torch.no_grad():
                for batch in loader:
                    batch = {
                        k: v.to("cuda") if isinstance(v, torch.Tensor) else v
                        for k, v in batch.items()
                    }
                    projected.extend(
                        self.surrogate.model.generate(
                            input_ids=batch["input_ids"],
                            attention_mask=batch["attention_mask"],
                            num_beams=1,
                            max_length=128,
                            repetition_penalty=1,
                            length_penalty=1.0,
                            early_stopping=True,
                            use_cache=True,
                            do_sample=False,
                            top_p=0.95,
                            top_k=50,
                            bad_words_ids=self.surrogate.bad_words,
                        )
                    )

            return [
                self.surrogate.data_generator._tokenizer.decode(
                    p, skip_special_tokens=True
                )
                for p in projected
            ]

        return Seq2SeqSpecificSurrogateGenerator(self.surrogate, self.tokenizer, fwd)

    # def validation_step(self, batch, batch_idx):
    #     inputs = {"input_ids": batch[0], "attention_mask": batch[1], "labels": batch[2]}
    #
    #     outputs = self(**inputs)
    #     tmp_eval_loss, logits = outputs[:2]
    #     preds = logits.detach().cpu().numpy()
    #     out_label_ids = inputs["labels"].detach().cpu().numpy()
    #
    #     return {"val_loss": tmp_eval_loss.detach().cpu(), "pred": preds, "target": out_label_ids}
    #
    # def test_step(self, batch, batch_idx):
    #     return self.validation_step(batch, batch_idx)

    def _eval_end(self, outputs):
        val_loss_mean = (
            torch.stack([x["val_loss"] for x in outputs]).mean().detach().cpu().item()
        )
        preds = np.concatenate([x["pred"] for x in outputs], axis=0)

        if self.hparams.glue_output_mode == "classification":
            preds = np.argmax(preds, axis=1)
        elif self.hparams.glue_output_mode == "regression":
            preds = np.squeeze(preds)

        out_label_ids = np.concatenate([x["target"] for x in outputs], axis=0)
        out_label_list = [[] for _ in range(out_label_ids.shape[0])]
        preds_list = [[] for _ in range(out_label_ids.shape[0])]

        results = {
            **{"val_loss": val_loss_mean},
            **compute_metrics("mnli", preds, out_label_ids),
        }

        ret = {k: v for k, v in results.items()}
        ret["log"] = results
        return ret, preds_list, out_label_list

    # def validation_epoch_end(self, outputs: list) -> dict:
    #     ret, preds, targets = self._eval_end(outputs)
    #     logs = ret["log"]
    #     return {"val_loss": logs["val_loss"], "log": logs, "progress_bar": logs}
    #
    # def test_epoch_end(self, outputs):
    #     ret, predictions, targets = self._eval_end(outputs)
    #     logs = ret["log"]
    #     return {"avg_test_loss": logs["val_loss"], "log": logs, "progress_bar": logs}

    def get_dataloader(self, type_path: str, batch_size: int) -> DataLoader:
        ds = AutoLoadDataset(self.reader, self.data_generator)
        ds.read(type_path)
        data_loader = DataLoader(
            ds,
            batch_size=batch_size,
            collate_fn=self.data_generator.collate_fn,
            shuffle=False,
        )
        return data_loader

    def train_dataloader(self) -> DataLoader:
        dataloader = self.get_dataloader(
            self.hparams.train_path, batch_size=self.hparams.train_batch_size
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

    @staticmethod
    def add_model_specific_args(parser, root_dir):
        # Add NER specific options
        BaseTransformer.add_model_specific_args(parser, root_dir)
        parser.add_argument(
            "--max_seq_length",
            default=1024,
            type=int,
            help="The maximum total input sequence length after tokenization. Sequences longer "
            "than this will be truncated, sequences shorter will be padded.",
        )

        parser.add_argument("--surrogate", required=True, type=str)

        parser.add_argument(
            "--train_path", type=str, required=True, help="Path to training data file"
        )

        parser.add_argument(
            "--val_path", type=str, required=False, help="Path to validation data file"
        )

        parser.add_argument(
            "--test_path", type=str, required=False, help="Path to test data file"
        )

        return parser


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    add_generic_args(parser, os.getcwd())
    parser = GLUETransformer.add_model_specific_args(parser, os.getcwd())
    args = parser.parse_args()

    # If output_dir not provided, a folder will be generated in pwd
    if args.output_dir is None:
        args.output_dir = os.path.join(
            "./results",
            f"{time.strftime('%Y%m%d_%H%M%S')}",
        )
        os.makedirs(args.output_dir)

    model = GLUETransformer(args)
    trainer = generic_train(model, args, val_percent_check=0)

    # Optionally, predict on dev set and write to output_dir
    if args.do_predict:
        checkpoints = list(
            sorted(
                glob.glob(
                    os.path.join(args.output_dir, "checkpointepoch=*.ckpt"),
                    recursive=True,
                )
            )
        )
        model = model.load_from_checkpoint(checkpoints[-1])
        trainer.test(model)
