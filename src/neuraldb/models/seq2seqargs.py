import logging
import os
import json
from collections import defaultdict
from pathlib import Path

import torch
import transformers
from similarity.normalized_levenshtein import NormalizedLevenshtein
from torch.utils.data import DataLoader
from transformers import get_linear_schedule_with_warmup

from neuraldb.dataset.base_reader import (
    NeuralDatabaseDatasetReader,
    NeuralDatabaseDatasetPipelineReader,
    NeuralDatabaseDatasetPipelineSSGReader, NeuralDatabaseV1DatasetReader,
)
from neuraldb.dataset.e2e_reader.v0_2_database_reader import V2DatabaseSpecificReader
from neuraldb.dataset.e2e_reader.v0_4_database_reader import V4DatabaseSpecificReader
from neuraldb.dataset.e2e_reader.v0_5_database_reader import V5DatabaseSpecificReader
from neuraldb.dataset.e2e_reader.v1_0_database_reader import V10DatabaseSpecificReader
from neuraldb.dataset.generic_dataset import GenericDataset
from neuraldb.dataset.e2e_generator.seq2seq_reader import Seq2SeqSpecificGenerator, V1Seq2SeqSpecificGenerator
from neuraldb.scoring.r_precision import f1
from neuraldb.dataset.search_engines.bm25 import BM25SearchEngine
from neuraldb.dataset.search_engines.return_all import ReturnAll
from neuraldb.dataset.search_engines.tfidf import TFIDFSearchEngine
from transformer_base import BaseTransformer

logger = logging.getLogger(__name__)


def save_json(content, path):
    with open(path, "w") as f:
        json.dump(content, f, indent=4)


def save_json_test(content, path):
    with open(path, "a") as f:
        f.write(json.dumps(content, indent=None, default=str) + "\n")


class Seq2seqTrainer(BaseTransformer):
    def __init__(self, hparams):
        transformers.tokenization_t5.T5Tokenizer.max_model_input_sizes[
            "t5-base"
        ] = hparams.max_source_length
        super().__init__(
            hparams,
            num_labels=None,
            n_positions=hparams.max_source_length,
            model_max_length=hparams.max_source_length,
        )
        self.em = 0
        self.source_length = self.hparams.max_source_length
        self.target_length = self.hparams.max_target_length
        self.output_dir = self.hparams.output_dir
        self.metrics_save_path = Path(self.output_dir) / "metrics.json"
        self.test_metrics_save_path = Path(self.output_dir) / "metrics_test_ssg.jsonl"

        self.hparams_save_path = Path(self.output_dir) / "hparams.pkl"
        self.metrics = {"validation": []}

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
        self.search_retriever = None
        self.data_generator = self.construct_generator()
        if hasattr(self.hparams, "retriever") and self.hparams.retriever == "pipeline":
            self.reader = NeuralDatabaseDatasetPipelineReader(self.data_generator)
        elif (
            hasattr(self.hparams, "test_path")
            and self.hparams.test_path is not None
            and "ssg" in self.hparams.test_path
        ) or (hasattr(self.hparams, "retriever") and self.hparams.retriever == "ssg"):
            self.reader = NeuralDatabaseDatasetPipelineSSGReader(self.data_generator)
            self.test_metrics_save_path = Path(self.output_dir) / (
                "metrics_test_" + os.path.basename(self.hparams.test_path)
            )
        else:
            self.data_reader = self.get_dataset_reader(self.hparams.dataset_version)
            self.search_retriever = self.construct_retriever(
                self.hparams.retriever
                if hasattr(self.hparams, "retriever")
                else "tfidf"
            )
            self.data_generator = self.construct_generator()
            if "v1" in self.hparams.dataset_version or "v2" in self.hparams.dataset_version:
                self.reader = NeuralDatabaseV1DatasetReader(
                    self.data_reader, self.data_generator
                )
            else:
                self.reader = NeuralDatabaseDatasetReader(
                    self.data_reader, self.data_generator
                )

        self.model.resize_token_embeddings(len(self.tokenizer))

    def get_dataset_reader(self, version):
        print(f"using dataset reader {version}")
        if version == "v0.2":
            return V2DatabaseSpecificReader(max_queries=self.hparams.max_queries)
        elif version == "v0.4":
            return V4DatabaseSpecificReader(
                max_queries=self.hparams.max_queries,
                max_list_len=10 if not hasattr(self.hparams, "external_test") else None,
                filter_types=set(self.hparams.filter)
                if hasattr(self.hparams, "filter")
                and self.hparams.filter is not None
                and not hasattr(self.hparams, "external_test")
                else None,
            )
        elif version == "v0.5":
            return V5DatabaseSpecificReader(
                max_queries=self.hparams.max_queries,
                max_list_len=50 if not hasattr(self.hparams, "external_test") else None,
                filter_types=set(self.hparams.filter)
                if hasattr(self.hparams, "filter")
                and self.hparams.filter is not None
                and not hasattr(self.hparams, "external_test")
                else None,
            )
        elif version.startswith("v1.") or version.startswith("v2."):
            return V10DatabaseSpecificReader(
                max_queries=self.hparams.max_queries,
                max_list_len=50 if not hasattr(self.hparams, "external_test") else None,
                filter_types=set(self.hparams.filter)
                if hasattr(self.hparams, "filter")
                   and self.hparams.filter is not None
                   and not hasattr(self.hparams, "external_test")
                else None,
            )

    def construct_retriever(self, search_engine="tfidf"):
        if search_engine == "tfidf":
            return TFIDFSearchEngine(50 if "large" in self.hparams.output_dir else 5)
        elif search_engine == "all":
            return ReturnAll()
        elif search_engine == "bm25":
            return BM25SearchEngine()

    def construct_generator(self):
        if "v1" in self.hparams.dataset_version or "v2" in self.hparams.dataset_version:
            return V1Seq2SeqSpecificGenerator(
                self.tokenizer,
                update_search=self.search_retriever,
                context_limit=self.source_length,
                answer_limit=self.target_length,
                test_mode=hasattr(self.hparams, "external_test")
                          and self.hparams.external_test,
                is_oracle=hasattr(self.hparams, "oracle") and self.hparams.oracle,
                iterate=hasattr(self.hparams, "iterate") and self.hparams.iterate,
            )
        else:
            return Seq2SeqSpecificGenerator(
                self.tokenizer,
                update_search=self.search_retriever,
                context_limit=self.source_length,
                answer_limit=self.target_length,
                test_mode=hasattr(self.hparams, "external_test")
                and self.hparams.external_test,
                is_oracle=hasattr(self.hparams, "oracle") and self.hparams.oracle,
                iterate=hasattr(self.hparams, "iterate") and self.hparams.iterate,
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
        self.trainer.total_loss = getattr(self.trainer, "total_loss", 0.0) + loss.item()
        self.trainer.avg_loss = (
            loss.item()
        )  # self.trainer.total_loss/((batch_idx+1)*self.hparams.train_batch_size)
        tensorboard_logs = {"train_loss": loss.item()}

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
            # print(s)
            # print(pred +' : '+t)
            if self.data_generator.list_sep in t:
                predicted = [
                    a.strip().lower() for a in pred.split(self.data_generator.list_sep)
                ]
                actual = [
                    a.strip().lower() for a in t.split(self.data_generator.list_sep)
                ]
                em += f1(actual, predicted)
            else:
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
            self.tokenizer.decode(t, skip_special_tokens=True)
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
        metadata = []
        for batch in outputs:
            sources.extend(batch["sources"])
            targets.extend(batch["targets"])
            preds.extend(batch["preds"])
            metadata.extend(batch["metadata"])

        em = 0.0
        strict_em = 0.0

        strict_big_score_breakdown = defaultdict(lambda: defaultdict(list))
        strict_score_breakdown = defaultdict(int)

        big_score_breakdown = defaultdict(lambda: defaultdict(list))
        score_breakdown = defaultdict(int)
        type_breakdown = defaultdict(int)

        output = []
        for s, pred, t, meta in zip(sources, preds, targets, metadata):
            pred = pred.strip()
            t = t.strip()
            if self.data_generator.list_sep in t or meta["query_type"] == "set":

                predicted = [
                    a.strip().lower() for a in pred.split(self.data_generator.list_sep)
                ]
                actual = [
                    a.strip().lower() for a in t.split(self.data_generator.list_sep)
                ]

                local_score = f1(actual, predicted)
                local_score_strict = local_score
            else:
                local_score_strict = 1.0 if pred == t else 0.0

                if (
                    t in self.data_generator.special_labels
                    or meta["query_type"] == "count"
                ):
                    local_score = 1.0 if pred == t else 0.0
                else:
                    local_score = normalized_levenshtein.similarity(pred, t)

            score_breakdown[meta["relation_type"]] += local_score
            big_score_breakdown["relation_type"][meta["relation_type"]].append(
                local_score
            )
            big_score_breakdown["query_type"][meta["query_type"]].append(local_score)

            strict_score_breakdown[meta["relation_type"]] += local_score_strict
            strict_big_score_breakdown["relation_type"][meta["relation_type"]].append(
                local_score_strict
            )
            strict_big_score_breakdown["query_type"][meta["query_type"]].append(
                local_score_strict
            )

            em += local_score
            strict_em += local_score_strict

            type_breakdown[meta["relation_type"]] += 1.0

            output.append([pred, t, local_score, local_score_strict, meta])

        metrics = {
            "epoch": self.trainer.current_epoch,
            "EM": float(em) / len(preds),
            "strict_EM": float(em) / len(preds),
            "scores": {k: v for k, v in score_breakdown.items()},
            "strict_scores": {k: v for k, v in strict_score_breakdown.items()},
            "types": {k: v for k, v in type_breakdown.items()},
            "breakdown": {k: dict(v) for k, v in big_score_breakdown.items()},
            "strict_breakdown": {
                k: dict(v) for k, v in strict_big_score_breakdown.items()
            },
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
        if isinstance(self.reader, NeuralDatabaseDatasetPipelineSSGReader):
            self.test_metrics_save_path = Path(self.output_dir) / (
                "metrics_test_" + os.path.basename(self.hparams.test_path)
            )

        self.metrics = {
            "test": {
                k: (v.item() if "item" in dir(v) else v)
                for k, v in latest_metrics.items()
                if k != "log"
            }
        }
        save_json_test(self.metrics, self.test_metrics_save_path)

    def get_dataloader(
        self, type_path: str, batch_size: int, shuffle: bool = False
    ) -> DataLoader:
        ds = GenericDataset(self.reader, self.data_generator)
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

        parser.add_argument(
            "--max_source_length",
            default=256,
            type=int,
            help="The maximum total input sequence length after tokenization. Sequences longer "
            "than this will be truncated, sequences shorter will be padded.",
        )

        parser.add_argument(
            "--max_target_length",
            default=48,
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
            "--dataset_version", type=str, required=True, help="Dataset version to read"
        )

        parser.add_argument(
            "--retriever", type=str, default="tfidf", help="Dataset retriever to use"
        )

        parser.add_argument(
            "--max_queries",
            type=int,
            required=False,
            help="Maximum number of queries to load for each database",
        )

        parser.add_argument(
            "--filter", type=str, nargs="*", help="Query or answer types to skip"
        )

        parser.add_argument("--oracle", action="store_true")

        parser.add_argument("--iterate", action="store_true")

        return parser
