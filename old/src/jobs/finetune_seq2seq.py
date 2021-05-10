import argparse
import os

import submitit

from jobs.submit_wrapper import SLURMTrainingWrapper
from neuraldb.models.seq2seqargs import Seq2seqTrainer
from lightning_base import add_generic_args

if __name__ == "__main__":
    model_cls = Seq2seqTrainer
    parser = argparse.ArgumentParser()
    add_generic_args(parser, None)
    parser = model_cls.add_model_specific_args(parser, os.getcwd())
    args = parser.parse_args()

    executor = submitit.SlurmExecutor(folder="logs_training", max_num_timeout=10)
    executor.update_parameters(time=60*24,
                               partition="dev",
                               gpus_per_node=args.n_gpu,
                               nodes=1,
                               ntasks_per_node=1,
                               constraint="volta32gb",
                               gres=f"gpu:{args.n_gpu}",
                               mem_per_cpu=32,
                               cpus_per_task=8)

    training_callable = SLURMTrainingWrapper(model_cls,args)
    job = executor.submit(training_callable, args.output_dir)