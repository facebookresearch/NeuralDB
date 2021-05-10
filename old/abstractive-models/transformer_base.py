import argparse
import logging
import os
import random
from typing import Optional, Union, Callable, Dict

import numpy as np
import pytorch_lightning as pl
import torch
from transformers import (
    AdamW,
    AutoConfig,
    AutoModelWithLMHead,
    AutoTokenizer,
    get_linear_schedule_with_warmup,
)

logger = logging.getLogger(__name__)


def set_seed(args: argparse.Namespace):
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if args.n_gpu > 0:
        torch.cuda.manual_seed_all(args.seed)


class BaseTransformer(pl.LightningModule):
    def __init__(self, hparams: argparse.Namespace, num_labels=None, **config_kwargs):
        "Initialize a model."

        super().__init__()
        self.hparams = hparams
        cache_dir = self.hparams.cache_dir if self.hparams.cache_dir else None
        self.config = AutoConfig.from_pretrained(
            self.hparams.config_name if self.hparams.config_name else self.hparams.model_name_or_path,
            **({"num_labels": num_labels} if num_labels is not None else {}),
            cache_dir=cache_dir,
            **config_kwargs,
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.hparams.tokenizer_name if self.hparams.tokenizer_name else self.hparams.model_name_or_path,
            cache_dir=cache_dir,
            **config_kwargs
        )

        self.model = self.construct_model(cache_dir)

    def construct_model(self,cache_dir):
        return AutoModelWithLMHead.from_pretrained(
            self.hparams.model_name_or_path,
            config=self.config,
            cache_dir=cache_dir,
        )

    @classmethod
    def load_from_checkpoint(
            cls,
            checkpoint_path: str,
            map_location: Optional[Union[Dict[str, str], str, torch.device, int, Callable]] = None,
            tags_csv: Optional[str] = None,
            *args, **kwargs
    ) -> 'LightningModule':
        r"""
        Primary way of loading a model from a checkpoint. When Lightning saves a checkpoint
        it stores the hyperparameters in the checkpoint if you initialized your :class:`LightningModule`
        with an argument called ``hparams`` which is a :class:`~argparse.Namespace`
        (output of :meth:`~argparse.ArgumentParser.parse_args` when parsing command line arguments).

        Example:
            .. code-block:: python

                from argparse import Namespace
                hparams = Namespace(**{'learning_rate': 0.1})

                model = MyModel(hparams)

                class MyModel(LightningModule):
                    def __init__(self, hparams):
                        self.learning_rate = hparams.learning_rate

        Args:
            checkpoint_path: Path to checkpoint.
            model_args: Any keyword args needed to init the model.
            map_location:
                If your checkpoint saved a GPU model and you now load on CPUs
                or a different number of GPUs, use this to map to the new setup.
                The behaviour is the same as in :func:`torch.load`.
            tags_csv: Optional path to a .csv file with two columns (key, value)
                as in this example::

                    key,value
                    drop_prob,0.2
                    batch_size,32

                You most likely won't need this since Lightning will always save the hyperparameters
                to the checkpoint.
                However, if your checkpoint weights don't have the hyperparameters saved,
                use this method to pass in a .csv file with the hparams you'd like to use.
                These will be converted into a :class:`~argparse.Namespace` and passed into your
                :class:`LightningModule` for use.

        Return:
            :class:`LightningModule` with loaded weights and hyperparameters (if available).

        Example:
            .. code-block:: python

                # load weights without mapping ...
                MyLightningModule.load_from_checkpoint('path/to/checkpoint.ckpt')

                # or load weights mapping all weights from GPU 1 to GPU 0 ...
                map_location = {'cuda:1':'cuda:0'}
                MyLightningModule.load_from_checkpoint(
                    'path/to/checkpoint.ckpt',
                    map_location=map_location
                )

                # or load weights and hyperparameters from separate files.
                MyLightningModule.load_from_checkpoint(
                    'path/to/checkpoint.ckpt',
                    tags_csv='/path/to/hparams_file.csv'
                )

                # or load passing whatever args the model takes to load
                MyLightningModule.load_from_checkpoint(
                    'path/to/checkpoint.ckpt',
                    learning_rate=0.1,
                    layers=2,
                    pretrained_model=some_model
                )

                # predict
                pretrained_model.eval()
                pretrained_model.freeze()
                y_hat = pretrained_model(x)
        """
        if map_location is not None:
            checkpoint = torch.load(checkpoint_path, map_location=map_location)
        else:
            checkpoint = torch.load(checkpoint_path, map_location=lambda storage, loc: storage)

        for k,v in kwargs.items():
            checkpoint['hparams'][k] = v

        model = cls._load_model_state(checkpoint, *args, **kwargs)
        return model

    def is_logger(self):
        return self.trainer.proc_rank <= 0

    def configure_optimizers(self):
        "Prepare optimizer and schedule (linear warmup and decay)"

        model = self.model
        no_decay = ["bias", "LayerNorm.weight"]
        optimizer_grouped_parameters = [
            dict(params=[p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)],
                 weight_decay=self.hparams.weight_decay),
            {
                "params": [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)],
                "weight_decay": 0.0,
            },
        ]
        optimizer = AdamW(optimizer_grouped_parameters, lr=self.hparams.learning_rate, eps=self.hparams.adam_epsilon)
        self.opt = optimizer
        return [optimizer]

    def optimizer_step(self, epoch, batch_idx, optimizer, optimizer_idx, second_order_closure=None):
        if self.trainer.use_tpu:
            xm.optimizer_step(optimizer)
        else:
            optimizer.step()
        optimizer.zero_grad()
        self.lr_scheduler.step()

    def get_tqdm_dict(self):
        avg_loss = getattr(self.trainer, "avg_loss", 0.0)
        tqdm_dict = {"loss": "{:.3f}".format(avg_loss), "lr": self.lr_scheduler.get_last_lr()[-1]}
        return tqdm_dict

    def test_step(self, batch, batch_nb):
        return self.validation_step(batch, batch_nb)

    def train_dataloader(self):
        train_batch_size = self.hparams.train_batch_size
        dataloader = self.load_dataset("train", train_batch_size)

        t_total = (
                (len(dataloader.dataset) // (train_batch_size * max(1, self.hparams.n_gpu)))
                // self.hparams.gradient_accumulation_steps
                * float(self.hparams.num_train_epochs)
        )
        scheduler = get_linear_schedule_with_warmup(
            self.opt, num_warmup_steps=self.hparams.warmup_steps, num_training_steps=t_total
        )
        self.lr_scheduler = scheduler
        return dataloader

    def val_dataloader(self):
        return self.load_dataset("dev", self.hparams.eval_batch_size)

    def test_dataloader(self):
        return self.load_dataset("test", self.hparams.eval_batch_size)

    def _feature_file(self, mode):
        return os.path.join(
            self.hparams.data_dir,
            "cached_{}_{}_{}".format(
                mode,
                list(filter(None, self.hparams.model_name_or_path.split("/"))).pop(),
                str(self.hparams.max_seq_length),
            ),
        )

    @staticmethod
    def add_model_specific_args(parser, root_dir):
        parser.add_argument(
            "--model_name_or_path",
            default=None,
            type=str,
            required=True,
            help="Path to pretrained model or model identifier from huggingfae.co/models",
        )
        parser.add_argument(
            "--config_name", default="", type=str, help="Pretrained config name or path if not the same as model_name"
        )
        parser.add_argument(
            "--tokenizer_name",
            default="",
            type=str,
            help="Pretrained tokenizer name or path if not the same as model_name",
        )
        parser.add_argument(
            "--cache_dir",
            default="",
            type=str,
            help="Where do you want to store the pre-trained models downloaded from s3",
        )
        parser.add_argument("--learning_rate", default=5e-5, type=float, help="The initial learning rate for Adam.")
        parser.add_argument("--weight_decay", default=0.0, type=float, help="Weight decay if we apply some.")
        parser.add_argument("--adam_epsilon", default=1e-8, type=float, help="Epsilon for Adam optimizer.")
        parser.add_argument("--warmup_steps", default=0, type=int, help="Linear warmup over warmup_steps.")
        parser.add_argument(
            "--num_train_epochs", default=3, type=int, help="Total number of commands epochs to perform."
        )

        parser.add_argument("--train_batch_size", default=100, type=int)
        parser.add_argument("--eval_batch_size", default=100, type=int)
        parser.add_argument("--train_percentage", type=float, default=1, help="percentage of data to load")


class LoggingCallback(pl.Callback):
    def on_validation_end(self, trainer: pl.Trainer, pl_module: pl.LightningModule):
        logger.info("***** Validation results *****")
        if pl_module.is_logger():
            metrics = trainer.callback_metrics
            # Log results
            for key in sorted(metrics):
                if key not in ["log", "progress_bar"]:
                    logger.info("{} = {}\n".format(key, str(metrics[key])))

    def on_test_end(self, trainer: pl.Trainer, pl_module: pl.LightningModule):
        logger.info("***** Test results *****")

        if pl_module.is_logger():
            metrics = trainer.callback_metrics

            # Log and save results to file
            output_test_results_file = os.path.join(pl_module.hparams.output_dir, "test_results.txt")
            with open(output_test_results_file, "w") as writer:
                for key in sorted(metrics):
                    if key not in ["log", "progress_bar"]:
                        logger.info("{} = {}\n".format(key, str(metrics[key])))
                        writer.write("{} = {}\n".format(key, str(metrics[key])))


def add_generic_args(parser):
    parser.add_argument(
        "--output_dir",
        default=None,
        type=str,
        required=True,
        help="The output directory where the model predictions and checkpoints will be written.",
    )

    parser.add_argument(
        "--fp16",
        action="store_true",
        help="Whether to use 16-bit (mixed) precision (through NVIDIA apex) instead of 32-bit",
    )

    parser.add_argument(
        "--fp16_opt_level",
        type=str,
        default="O1",
        help="For fp16: Apex AMP optimization level selected in ['O0', 'O1', 'O2', and 'O3']."
             "See details at https://nvidia.github.io/apex/amp.html",
    )

    parser.add_argument("--n_gpu", type=int, default=1)
    parser.add_argument("--n_tpu_cores", type=int, default=0)
    parser.add_argument("--max_grad_norm", default=1.0, type=float, help="Max gradient norm.")
    parser.add_argument("--do_train", action="store_true", help="Whether to run commands.")
    parser.add_argument("--do_predict", action="store_true", help="Whether to run predictions on the test set.")
    parser.add_argument(
        "--gradient_accumulation_steps",
        type=int,
        default=1,
        help="Number of updates steps to accumulate before performing a backward/update pass.",
    )

    parser.add_argument("--seed", type=int, default=42, help="random seed for initialization")
    parser.add_argument("--train_percentage", type=float, default=1, help="percentage of data to load")
    parser.add_argument("--dev_percentage", type=float, default=1, help="percentage of data to load")
    parser.add_argument("--val_check_interval", type=float, default=None)


def generic_train(model: BaseTransformer, args: argparse.Namespace):
    # init model
    set_seed(args)

    if os.path.exists(args.output_dir) and os.listdir(args.output_dir) and args.do_train:
        raise ValueError("Output directory ({}) already exists and is not empty.".format(args.output_dir))

    checkpoint_callback = pl.callbacks.ModelCheckpoint(
        filepath=args.output_dir, prefix="checkpoint", monitor="val_loss", mode="min", save_top_k=5
    )

    train_params = dict(
        accumulate_grad_batches=args.gradient_accumulation_steps,
        gpus=args.n_gpu,
        max_epochs=args.num_train_epochs,
        early_stop_callback=False,
        gradient_clip_val=args.max_grad_norm,
        checkpoint_callback=checkpoint_callback,
        callbacks=[LoggingCallback()],

    )

    if hasattr(args,"val_check_interval") and args.val_check_interval is not None:
        train_params["val_check_interval"] = args.val_check_interval

    if args.fp16:
        train_params["use_amp"] = args.fp16
        train_params["amp_level"] = args.fp16_opt_level

    if args.n_tpu_cores > 0:
        global xm

        train_params["num_tpu_cores"] = args.n_tpu_cores
        train_params["gpus"] = 0

    if args.n_gpu > 1:
        train_params["distributed_backend"] = "ddp"

    trainer = pl.Trainer(**train_params)

    if args.do_train:
        trainer.fit(model)

    return trainer
