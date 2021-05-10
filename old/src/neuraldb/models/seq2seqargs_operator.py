import logging
import os
import json
from collections import defaultdict
from pathlib import Path

import torch
from similarity.normalized_levenshtein import NormalizedLevenshtein
from torch.utils.data import DataLoader
from transformers import (
    get_linear_schedule_with_warmup,
    T5ForConditionalGeneration,
    T5Config,
)

from neuraldb.dataset.base_reader import NeuralDatabaseDatasetReader
from neuraldb.dataset.e2e_reader.v0_2_database_reader import V2DatabaseSpecificReader
from neuraldb.dataset.e2e_reader.v0_4_database_reader import V4DatabaseSpecificReader
from neuraldb.dataset.e2e_reader.v0_5_database_reader import V5DatabaseSpecificReader
from neuraldb.dataset.generic_dataset import GenericDataset
from neuraldb.dataset.e2e_generator.seq2seq_reader import Seq2SeqSpecificGenerator
from neuraldb.dataset.nuo_generator.nuo_seq2seq_generator import (
    NUOSeq2SeqSpecificGenerator,
)
from neuraldb.dataset.nuo_generator.v1nuo_seq2seq_generator import V1NUOSeq2SeqSpecificGenerator
from neuraldb.scoring.r_precision import f1
from neuraldb.dataset.search_engines.tfidf import TFIDFSearchEngine
from neuraldb.dataset.unary_operator_reader import UnaryOperatorReader
from transformer_base import BaseTransformer

logger = logging.getLogger(__name__)


def save_json(content, path):
    with open(path, "w") as f:
        json.dump(content, f, indent=4)


def save_json_test(content, path):
    with open(path, "a") as f:
        f.write(json.dumps(content, indent=None) + "\n")


class Seq2seqOperatorTrainer(BaseTransformer):
    def __init__(self, hparams):
        super().__init__(hparams, num_labels=None)
        self.em = 0
        self.source_length = self.hparams.max_source_length
        self.target_length = self.hparams.max_target_length
        self.output_dir = self.hparams.output_dir
        self.metrics_save_path = Path(self.output_dir) / "metrics.json"
        self.test_metrics_save_path = Path(self.output_dir) / "metrics_test.jsonl"
        self.hparams_save_path = Path(self.output_dir) / "hparams.pkl"
        self.metrics = {"validation": []}
        self.generate_random = self.hparams.generate_random if "generate_random" in self.hparams else False

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

        special_tokens = []
        for i in range(0, 101):
            special_tokens.append("<extra_id_" + str(i) + ">")

        special_tokens.extend(["NDB:"])
        self.tokenizer.add_special_tokens({"additional_special_tokens": special_tokens})

        self.bad_words = [
            [self.tokenizer.convert_tokens_to_ids(bad_word)]
            for bad_word in self.tokenizer.additional_special_tokens
        ]

        self.data_generator = self.construct_generator()

        self.reader = UnaryOperatorReader(self.data_generator)

        self.model.resize_token_embeddings(len(self.tokenizer))

    def construct_model(self, cache_dir):
        if not hasattr(self.hparams, "random_init") or not self.hparams.random_init:
            return super(Seq2seqOperatorTrainer, self).construct_model(cache_dir)

        print("NO PRETRAIN")
        config = T5Config(
            vocab_size=32128,
            n_positions=512,
            d_model=768,
            d_kv=64,
            d_ff=3072,
            num_layers=12,
            num_heads=12,
            relative_attention_num_buckets=32,
            dropout_rate=0.1,
            layer_norm_epsilon=1e-6,
            initializer_factor=1.0,
            is_encoder_decoder=True,
            pad_token_id=0,
            eos_token_id=1,
            decoder_start_token_id=0,
        )

        return T5ForConditionalGeneration(config=config)

    def construct_generator(self):
        return V1NUOSeq2SeqSpecificGenerator(
            self.tokenizer,
            context_limit=self.source_length,
            generate_random=self.generate_random,
            answer_limit=self.target_length,
            filter_types=set(self.hparams.filter)
            if hasattr(self.hparams, "filter")
            and self.hparams.filter is not None
            and not hasattr(self.hparams, "external_test")
            else None,
            test_mode=hasattr(self.hparams, "external_test"),
        )

    def forward(
        self,
        input_ids=None,
        inputs_embeds=None,
        attention_mask=None,
        decoder_input_ids=None,
        lm_labels=None,
        retriever_bias=None,
    ):
        if decoder_input_ids == None:
            return self.model(
                input_ids=input_ids,
                inputs_embeds=inputs_embeds,
                attention_mask=attention_mask,
                lm_labels=lm_labels,
            )
        else:
            if retriever_bias is not None:
                return self.model(
                    input_ids=input_ids,
                    inputs_embeds=inputs_embeds,
                    attention_mask=attention_mask,
                    decoder_input_ids=decoder_input_ids,
                    lm_labels=lm_labels,
                    retriever_bias=retriever_bias,
                )

            else:
                return self.model(
                    input_ids=input_ids,
                    inputs_embeds=inputs_embeds,
                    attention_mask=attention_mask,
                    decoder_input_ids=decoder_input_ids,
                    lm_labels=lm_labels,
                )

    def _step(self, batch):
        pad_token_id = self.tokenizer.pad_token_id

        if "bart" in self.hparams.model_name_or_path:
            lm_labels = batch["lm_labels"][:, :-1].contiguous()
            lm_labels = lm_labels[:, 1:].clone()
            lm_labels[lm_labels[:, 1:] == pad_token_id] = -100
            outputs = self(
                batch["input_ids"],
                attention_mask=batch["attention_mask"],
                decoder_input_ids=batch["input_ids"],
                lm_labels=lm_labels,
            )

        if "t5" in self.hparams.model_name_or_path:
            lm_labels = batch["decoder_input_ids"]
            lm_labels = lm_labels.clone()
            lm_labels[lm_labels == pad_token_id] = -100
            outputs = self(
                batch["input_ids"],
                attention_mask=batch["attention_mask"],
                lm_labels=lm_labels,
            )

        loss = outputs[0]

        return loss

    def training_step(self, batch, batch_idx):
        if batch_idx == 0:
            self.trainer.total_loss = 0
        loss = self._step(batch)
        self.trainer.total_loss = getattr(self.trainer, "total_loss", 0.0) + loss
        self.trainer.avg_loss = loss  # self.trainer.total_loss/((batch_idx+1)*self.hparams.train_batch_size)
        tensorboard_logs = {"train_loss": loss}

        if False and batch_idx % 25 == 0:
            with torch.no_grad():
                val = self.validation_step(batch, batch_idx)
                print("Checking model outputs:")
                for q, e, t, p in zip(
                    batch["debug_input_query"],
                    batch["debug_input_evidence"],
                    val["targets"],
                    val["preds"],
                ):
                    print("*" * 80)
                    print("Query: \t{}".format(q))
                    for score, evidence in e:
                        print("{} {}".format(score, evidence))
                    print("Target and predicted:\t ", t, p)
                    print("*" * 80)
        return {"loss": loss, "log": tensorboard_logs}

    def validation_step(self, batch, batch_idx):

        generated_ids = self.model.generate(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            num_beams=1,
            max_length=self.target_length,
            repetition_penalty=1,
            length_penalty=1.0,
            early_stopping=True,
            use_cache=True,
            do_sample=False,
            top_p=0.95,
            top_k=50,
            bad_words_ids=self.bad_words,
        )

        preds = [
            self.tokenizer.decode(g, skip_special_tokens=True) for g in generated_ids
        ]
        target = [
            self.tokenizer.decode(t, skip_special_tokens=True)
            for t in batch["decoder_input_ids"]
        ]
        loss = self._step(batch)
        sources = [self.tokenizer.decode(s) for s in batch["input_ids"]]

        return {"val_loss": loss, "sources": sources, "preds": preds, "targets": target}

    def validation_epoch_end(self, outputs):

        normalized_levenshtein = NormalizedLevenshtein()
        avg_loss = torch.stack([x["val_loss"] for x in outputs]).mean()
        tensorboard_logs = {"val_loss": avg_loss}

        preds = []
        targets = []
        sources = []
        ids = []
        for batch in outputs:
            sources.extend(batch["sources"])
            targets.extend(batch["targets"])
            preds.extend(batch["preds"])

        em = 0.0
        for s, pred, t in zip(sources, preds, targets):
            pred = pred.strip()
            t = t.strip()

            if t in self.data_generator.special_labels:
                if pred == t:
                    em += 1.0
            else:
                em += normalized_levenshtein.similarity(pred, t)

        if float(em) / len(preds) > self.em:
            self.em = float(em) / len(preds)
            self.trainer.save_checkpoint(self.output_dir + "/" + "best_em.ckpt")

        metrics = {
            "epoch": self.trainer.current_epoch,
            "avg_val_loss": avg_loss,
            "log": tensorboard_logs,
            "EM": float(em) / len(preds),
        }
        self.save_metrics(metrics, "validation")
        return metrics

    def test_step(self, batch, batch_idx):

        generated_ids = self.model.generate(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            num_beams=1,
            max_length=self.target_length,
            repetition_penalty=1,
            length_penalty=1.0,
            early_stopping=True,
            use_cache=True,
            do_sample=False,
            top_p=0.95,
            top_k=50,
            bad_words_ids=self.bad_words,
        )

        # loss = self._step(batch)

        preds = [
            self.tokenizer.decode(g, skip_special_tokens=True) for g in generated_ids
        ]


        target = [
            self.tokenizer.decode(t, skip_special_tokens=True) if t is not None else ""
            for t in batch["decoder_input_ids"]
        ]
        sources = [self.tokenizer.decode(s) for s in batch["input_ids"]]

        return {
            "sources": sources,
            "preds": preds,
            "targets": target,
            "metadata": batch["metadata"] if "metadata" in batch else None,
        }

    def test_epoch_end(self, outputs):

        normalized_levenshtein = NormalizedLevenshtein()

        preds = []
        targets = []
        sources = []
        meta = []
        for batch in outputs:
            sources.extend(batch["sources"])
            targets.extend(batch["targets"])
            preds.extend(batch["preds"])
            meta.extend(batch["metadata"])

        em = 0.0
        big_score_breakdown = defaultdict(lambda: defaultdict(list))
        output = []
        for s, pred, t, meta in zip(sources, preds, targets, meta):
            pred = pred.strip()
            t = t.strip()

            local_score = 0.0
            if t in self.data_generator.special_labels:
                if pred == t:
                    local_score = 1.0
            else:
                local_score = normalized_levenshtein.similarity(pred, t)

            em += local_score
            # big_score_breakdown["breakdown_prop"][
            #     meta["prop"] if "prop" in meta else meta["relation"]
            # ].append(local_score)
            # big_score_breakdown["breakdown_type"][meta["type"]].append(local_score)

            output.append([pred, t, local_score, meta])

        metrics = {
            "epoch": self.trainer.current_epoch,
            "EM": float(em) / len(preds),
            "breakdown": {k: dict(v) for k, v in big_score_breakdown.items()},
            "raw": output,
        }

        self.save_metrics_test(metrics, "test")
        return metrics

    def save_metrics(self, latest_metrics, type_path) -> None:
        self.metrics[type_path].append(
            {
                k: (v.item() if "item" in dir(v) else v)
                for k, v in latest_metrics.items()
                if k != "log"
            }
        )
        save_json(self.metrics, self.metrics_save_path)

    def save_metrics_test(self, latest_metrics, type_path) -> None:
        self.metrics = {
            "test": {
                k: (v.item() if "item" in dir(v) else v)
                for k, v in latest_metrics.items()
                if k != "log"
            }
        }
        save_json_test(self.metrics, self.test_metrics_save_path)

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
            percentage=self.hparams.train_percentage,
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

    @staticmethod
    def add_model_specific_args(parser, root_dir):
        BaseTransformer.add_model_specific_args(parser, root_dir)

        parser.add_argument("--random_init", action="store_true")

        parser.add_argument(
            "--max_source_length",
            default=128,
            type=int,
            help="The maximum total input sequence length after tokenization. Sequences longer "
            "than this will be truncated, sequences shorter will be padded.",
        )

        parser.add_argument(
            "--max_target_length",
            default=64,
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

        parser.add_argument(
            "--filter", type=str, nargs="*", help="Query or answer types to skip"
        )

        parser.add_argument(
            "--generate_random", action='store_true')


        return parser
