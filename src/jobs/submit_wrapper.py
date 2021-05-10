import glob
import os
import sys

import submitit
import time

from pathlib import Path
import submitit
import pytorch_lightning as pl
from lightning_base import LoggingCallback, set_seed


class SLURMTrainingWrapper:

    def __init__(self, model_cls, args):
        self.model = None
        self.model_cls = model_cls
        self.args = args

    def __call__(self, checkpoint_path:str):
        args = self.args

        if not args.output_dir:
            args.output_dir = os.path.join(
                "./results",
                f"{args.task}_{time.strftime('%Y%m%d_%H%M%S')}",
            )
            os.makedirs(args.output_dir)

        # init model
        set_seed(args)

        checkpt = None
        if os.path.exists(args.output_dir) and os.listdir(args.output_dir) and args.do_train:
            if os.path.exists(args.output_dir+"/best_em.ckpt"):
                print("Best epoch already exists")
                sys.exit(0)
            elif os.path.exists(args.output_dir + "/exit.ckpt"):
                checkpt = args.output_dir + "/exit.ckpt"

        self.model = self.model_cls(args)

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
            default_save_path=args.output_dir,
            resume_from_checkpoint=checkpt
        )

        if hasattr(args, "val_check_interval") and args.val_check_interval is not None:
            train_params["val_check_interval"] = args.val_check_interval

        if args.n_gpu > 1:
            train_params["distributed_backend"] = "ddp"

        trainer = pl.Trainer(**train_params)

        self.trainer = trainer

        trainer.fit(self.model)


    def checkpoint(self, checkpointpath: str) -> submitit.helpers.DelayedSubmission:
        # the checkpoint method is called asynchroneously when the slurm manager
        # sends a preemption signal, with the same arguments as the __call__ method
        # "self" is your callable, at its current state.
        # "self" therefore holds the current version of the model:
        # do whatever you need to do to dump it properly
        # this is an example that probably does not work

        self.trainer.save_checkpoint(self.args.output_dir+"/exit.ckpt")

        # create a new, clean (= no loaded model) NetworkTraining instance which
        # will be loaded when the job resumes, and will fetch the dumped model
        # (creating a new instance is not necessary but can avoid weird interactions
        # with the current instance)
        training_callable = SLURMTrainingWrapper(self.model_cls, self.args)
        # Resubmission to the queue is performed through the DelayedSubmission object
        return submitit.helpers.DelayedSubmission(training_callable, checkpointpath)