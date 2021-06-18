#
# Copyright (c) 2021 Facebook, Inc. and its affiliates.
#
# This file is part of NeuralDB.
# See https://github.com/facebookresearch/NeuralDB for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import os
from dataclasses import dataclass, field
from typing import Optional

import transformers
from transformers import (
    AutoConfig,
    AutoTokenizer,
    HfArgumentParser,
    set_seed,
    Seq2SeqTrainingArguments,
    AutoModelForSeq2SeqLM,
)

# import transformers.modelling.t5.tokenization_t5
import transformers.models.t5.tokenization_t5_fast
from transformers.trainer_utils import get_last_checkpoint, is_main_process

from neuraldb.dataset.data_collator_seq2seq import DataCollatorForSeq2SeqAllowMetadata
from neuraldb.dataset.instance_generator.externalir_generator import ExternalIRGenerator
from neuraldb.dataset.instance_generator.externalir_generator_maxtok import (
    ExternalIRGeneratorMaxTok,
)
from neuraldb.dataset.instance_generator.perfectir_generator import PerfectIRGenerator
from neuraldb.dataset.instance_generator.spj_generator import NeuralSPJGenerator
from neuraldb.dataset.instance_generator.subsampler import Subsampler
from neuraldb.dataset.instance_generator.wholedb_generator import WholeDBGenerator
from neuraldb.dataset.neuraldb_file_reader import NeuralDBFileReader
from neuraldb.dataset.seq2seq_dataset import Seq2SeqDataset
from neuraldb.evaluation.postprocess_baselines import get_baseline_evaluation
from neuraldb.evaluation.postprocess_spj import get_spj_evaluation
from neuraldb.modelling.fusion_in_decoder import T5MergeForConditionalGeneration
from neuraldb.modelling.neuraldb_trainer import NeuralDBTrainer
from neuraldb.util.log_helper import setup_logging

logger = logging.getLogger(__name__)


# transformers.tokenization_t5.T5Tokenizer.max_model_input_sizes[
#     "t5-base"
# ] = hparams.max_source_length


@dataclass
class ModelArguments:
    """
    Arguments pertaining to which model/config/tokenizer we are going to fine-tune from.
    """

    model_name_or_path: str = field(
        metadata={
            "help": "Path to pretrained model or model identifier from huggingface.co/modelling"
        }
    )
    config_name: Optional[str] = field(
        default=None,
        metadata={
            "help": "Pretrained config name or path if not the same as model_name"
        },
    )
    tokenizer_name: Optional[str] = field(
        default=None,
        metadata={
            "help": "Pretrained tokenizer name or path if not the same as model_name"
        },
    )
    cache_dir: Optional[str] = field(
        default=None,
        metadata={
            "help": "Path to directory to store the pretrained modelling downloaded from huggingface.co"
        },
    )
    model_revision: str = field(
        default="main",
        metadata={
            "help": "The specific model version to use (can be a branch name, tag name or commit id)."
        },
    )
    use_auth_token: bool = field(
        default=False,
        metadata={
            "help": "Will use the token generated when running `transformers-cli login` (necessary to use this script "
            "with private modelling)."
        },
    )


@dataclass
class DataTrainingArguments:
    instance_generator: Optional[str] = field(
        default=None, metadata={"help": "The instance generator perfectir/wholedb/spj"}
    )

    train_file: Optional[str] = field(
        default=None,
        metadata={"help": "The input training data file (a jsonlines or csv file)."},
    )
    validation_file: Optional[str] = field(
        default=None,
        metadata={
            "help": "An optional input evaluation data file to evaluate the metrics (rouge) on "
            "(a jsonlines or csv file)."
        },
    )
    test_file: Optional[str] = field(
        default=None,
        metadata={
            "help": "An optional input test data file to evaluate the metrics (rouge) on "
            "(a jsonlines or csv file)."
        },
    )
    overwrite_cache: bool = field(
        default=False,
        metadata={"help": "Overwrite the cached training and evaluation sets"},
    )
    preprocessing_num_workers: Optional[int] = field(
        default=None,
        metadata={"help": "The number of processes to use for the preprocessing."},
    )
    max_source_length: Optional[int] = field(
        default=1024,
        metadata={
            "help": "The maximum total input sequence length after tokenization. Sequences longer "
            "than this will be truncated, sequences shorter will be padded."
        },
    )
    max_target_length: Optional[int] = field(
        default=64,
        metadata={
            "help": "The maximum total sequence length for target text after tokenization. Sequences longer "
            "than this will be truncated, sequences shorter will be padded."
        },
    )
    val_max_target_length: Optional[int] = field(
        default=None,
        metadata={
            "help": "The maximum total sequence length for validation target text after tokenization. Sequences longer "
            "than this will be truncated, sequences shorter will be padded. Will default to `max_target_length`."
            "This argument is also used to override the ``max_length`` param of ``model.generate``, which is used "
            "during ``evaluate`` and ``predict``."
        },
    )
    pad_to_max_length: bool = field(
        default=False,
        metadata={
            "help": "Whether to pad all samples to model maximum sentence length. "
            "If False, will pad the samples dynamically when batching to the maximum length in the batch. More "
            "efficient on GPU but very bad for TPU."
        },
    )
    max_train_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes or quicker training, truncate the number of training examples to this "
            "value if set."
        },
    )
    max_val_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes or quicker training, truncate the number of validation examples to this "
            "value if set."
        },
    )
    max_test_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes or quicker training, truncate the number of test examples to this "
            "value if set."
        },
    )
    num_beams: Optional[int] = field(
        default=None,
        metadata={
            "help": "Number of beams to use for evaluation. This argument will be passed to ``model.generate``, "
            "which is used during ``evaluate`` and ``predict``."
        },
    )
    ignore_pad_token_for_loss: bool = field(
        default=True,
        metadata={
            "help": "Whether to ignore the tokens corresponding to padded labels in the loss computation or not."
        },
    )
    source_prefix: Optional[str] = field(
        default=None,
        metadata={
            "help": "A prefix to add before every source text (useful for T5 modelling)."
        },
    )
    predictions_file: Optional[str] = field(
        default=None, metadata={"help": "Save the predictions file"}
    )

    def __post_init__(self):
        if (
            self.train_file is None
            and self.validation_file is None
            and self.test_file is None
        ):
            raise ValueError(
                "Need either a dataset name or a training/validation file."
            )
        else:
            if self.train_file is not None:
                extension = self.train_file.split(".")[-1]
                assert extension in [
                    "jsonl"
                ], "`train_file` should be a csv or a json file."
            if self.validation_file is not None:
                extension = self.validation_file.split(".")[-1]
                assert extension in [
                    "jsonl"
                ], "`validation_file` should be a csv or a json file."
            if self.test_file is not None:
                extension = self.test_file.split(".")[-1]
                assert extension in [
                    "jsonl"
                ], "`test_file` should be a csv or a json file."

        if self.val_max_target_length is None:
            self.val_max_target_length = self.max_target_length


def get_generator(generator_name):
    if generator_name == "perfectir":
        return NeuralDBFileReader, PerfectIRGenerator, {}, get_baseline_evaluation
    elif generator_name == "externalir":
        return NeuralDBFileReader, ExternalIRGenerator, {}, get_baseline_evaluation
    elif generator_name == "externalir2":
        return (
            NeuralDBFileReader,
            ExternalIRGeneratorMaxTok,
            {},
            get_baseline_evaluation,
        )
    elif generator_name == "perfectirsubs":
        return (
            PerfectIRGenerator,
            {
                "subsampler": Subsampler(
                    {"argmin": 0.2, "argmax": 0.2, "bool": [0, 0, 0]}
                )
            },
            get_baseline_evaluation,
        )
    elif generator_name == "wholedb":
        return NeuralDBFileReader, WholeDBGenerator, {}, get_baseline_evaluation
    elif generator_name == "spj":
        return NeuralDBFileReader, NeuralSPJGenerator, {}, get_spj_evaluation
    elif generator_name == "spj_rand":
        return (
            NeuralDBFileReader,
            NeuralSPJGenerator,
            {"augment_training": True},
            get_spj_evaluation,
        )

    raise ValueError(f"Unregistered generator name: {generator_name}")


def dict_flatten(in_dict, dict_out=None, parent_key=None, separator="_"):
    if dict_out is None:
        dict_out = {}

    for k, v in in_dict.items():
        k = f"{parent_key}{separator}{k}" if parent_key else k
        if isinstance(v, dict):
            dict_flatten(in_dict=v, dict_out=dict_out, parent_key=k)
            continue

        dict_out[k] = v

    return dict_out


def flatten_dicts(metrics):
    return dict_flatten(metrics, separator=".")


def main():
    setup_logging()

    parser = HfArgumentParser(
        (ModelArguments, DataTrainingArguments, Seq2SeqTrainingArguments)
    )
    model_args, data_args, training_args = parser.parse_args_into_dataclasses()

    last_checkpoint = None
    if (
        os.path.isdir(training_args.output_dir)
        and training_args.do_train
        and not training_args.overwrite_output_dir
    ):
        last_checkpoint = get_last_checkpoint(training_args.output_dir)
        if last_checkpoint is None and len(os.listdir(training_args.output_dir)) > 0:
            raise ValueError(
                f"Output directory ({training_args.output_dir}) already exists and is not empty. "
                "Use --overwrite_output_dir to overcome."
            )
        elif (
            last_checkpoint is not None and training_args.resume_from_checkpoint is None
        ):
            logger.info(
                f"Checkpoint detected, resuming training at {last_checkpoint}. To avoid this behavior, change "
                "the `--output_dir` or add `--overwrite_output_dir` to train from scratch."
            )

    # Log on each process the small summary:
    logger.warning(
        f"Process rank: {training_args.local_rank}, device: {training_args.device}, n_gpu: {training_args.n_gpu}"
        + f"distributed training: {bool(training_args.local_rank != -1)}, 16-bits training: {training_args.fp16}"
    )
    # Set the verbosity to info of the Transformers logger (on main process only):
    if is_main_process(training_args.local_rank):
        transformers.utils.logging.set_verbosity_info()
        transformers.utils.logging.enable_default_handler()
        transformers.utils.logging.enable_explicit_format()

    logger.info(f"Training/evaluation parameters {training_args}")

    # Set seed before initializing model.
    set_seed(training_args.seed)

    data_files = {}
    if data_args.train_file is not None:
        data_files["train"] = data_args.train_file
    if data_args.validation_file is not None:
        data_files["validation"] = data_args.validation_file
    if data_args.test_file is not None:
        data_files["test"] = data_args.test_file

    transformers.models.t5.tokenization_t5_fast.T5TokenizerFast.max_model_input_sizes[
        model_args.model_name_or_path
    ] = data_args.max_source_length

    use_fid = False
    if "-fid" in model_args.model_name_or_path:
        model_args.model_name_or_path = model_args.model_name_or_path.replace(
            "-fid", ""
        )
        use_fid = True

    config_kwargs = {}
    if "t5" in model_args.model_name_or_path:
        config_kwargs.update({"n_positions": data_args.max_source_length})

    config = AutoConfig.from_pretrained(
        model_args.config_name
        if model_args.config_name
        else model_args.model_name_or_path,
        cache_dir=model_args.cache_dir,
        revision=model_args.model_revision,
        use_auth_token=True if model_args.use_auth_token else None,
        max_length=data_args.max_target_length,
        **config_kwargs,
    )

    tokenizer = AutoTokenizer.from_pretrained(
        model_args.tokenizer_name
        if model_args.tokenizer_name
        else model_args.model_name_or_path,
        cache_dir=model_args.cache_dir,
        use_fast=False,
        revision=model_args.model_revision,
        use_auth_token=True if model_args.use_auth_token else None,
    )

    if use_fid:
        AutoModelForSeq2SeqLM._model_mapping.update(
            {type(config): T5MergeForConditionalGeneration}
        )

    # Temporarily set max_target_length for training.
    max_target_length = data_args.max_target_length
    padding = "max_length" if data_args.pad_to_max_length else False

    reader_cls, generator_cls, generator_kwargs, evaluation_metrics = get_generator(
        data_args.instance_generator
    )

    generators = {}
    datasets = {}
    for split, path in data_files.items():
        generator = generator_cls(
            tokenizer,
            maximum_source_length=data_args.max_source_length,
            maximum_target_length=max_target_length,
            padding=padding,
            ignore_pad_token_for_loss=data_args.ignore_pad_token_for_loss,
            test_mode=(split != "train"),
            **generator_kwargs,
        )
        dataset_reader = reader_cls(instance_generator=generator)

        generators[split] = generator
        datasets[split] = Seq2SeqDataset(
            dataset_reader.read(path),
            auto_pad=generator.encode if not use_fid else generator.fusion_encode,
        )

    compute_metrics = evaluation_metrics(
        data_args,
        tokenizer,
        generators["validation"] if "validation" in generators else generators["test"],
    )
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_args.model_name_or_path,  # + ("-fid" if use_fid else ""),
        from_tf=bool(".ckpt" in model_args.model_name_or_path),
        config=config,
        cache_dir=model_args.cache_dir,
        revision=model_args.model_revision,
        use_auth_token=True if model_args.use_auth_token else None,
    )

    if training_args.label_smoothing_factor > 0 and not hasattr(
        model, "prepare_decoder_input_ids_from_labels"
    ):
        logger.warning(
            "label_smoothing is enabled but the `prepare_decoder_input_ids_from_labels` method is not defined for"
            f"`{model.__class__.__name__}`. This will lead to loss being calculated twice and will take up more memory"
        )

    # Data collator
    label_pad_token_id = (
        -100 if data_args.ignore_pad_token_for_loss else tokenizer.pad_token_id
    )
    data_collator = DataCollatorForSeq2SeqAllowMetadata(
        tokenizer,
        model=model,
        label_pad_token_id=label_pad_token_id,
        pad_to_multiple_of=8
        if training_args.fp16
        else (1024 if "led" in model_args.model_name_or_path else None),
    )
    model.resize_token_embeddings(len(tokenizer))

    if training_args.do_train or training_args.do_eval:
        # Initialize our Trainer
        trainer = NeuralDBTrainer(
            model=model,
            args=training_args,
            train_dataset=datasets["train"] if training_args.do_train else None,
            eval_dataset=datasets["validation"] if training_args.do_eval else None,
            tokenizer=tokenizer,
            data_collator=data_collator,
            compute_metrics=compute_metrics,
        )

    # Training
    if training_args.do_train:
        if last_checkpoint is not None:
            checkpoint = last_checkpoint
        elif os.path.isdir(model_args.model_name_or_path):
            checkpoint = model_args.model_name_or_path
        else:
            checkpoint = None
        train_result = trainer.train(resume_from_checkpoint=checkpoint)
        trainer.save_model()  # Saves the tokenizer too for easy upload

        metrics = train_result.metrics
        max_train_samples = (
            data_args.max_train_samples
            if data_args.max_train_samples is not None
            else len(datasets["train"])
        )
        metrics["train_samples"] = min(max_train_samples, len(datasets["train"]))

        trainer.log_metrics("train", metrics)
        trainer.save_metrics("train", metrics)
        trainer.save_state()

    # Evaluation
    if training_args.do_eval:
        logger.info("*** Evaluate ***")
        metrics = trainer.evaluate()
        trainer.log_metrics("eval", flatten_dicts(metrics))
        trainer.save_metrics("eval", metrics)

    if training_args.do_predict:
        logger.info("*** Test ***")

        compute_metrics = evaluation_metrics(data_args, tokenizer, generators["test"])
        tester = NeuralDBTrainer(
            model=model,
            args=training_args,
            eval_dataset=datasets["test"],
            tokenizer=tokenizer,
            data_collator=data_collator,
            compute_metrics=compute_metrics,
        )

        metrics = tester.evaluate()
        tester.log_metrics("test", flatten_dicts(metrics))
        tester.save_metrics("test", metrics)


def _mp_fn(index):
    # For xla_spawn (TPUs)
    main()


if __name__ == "__main__":
    main()
