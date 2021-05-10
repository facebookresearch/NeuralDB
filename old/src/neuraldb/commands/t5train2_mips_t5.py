import argparse
import glob

import os
from datetime import time

from lightning_base import add_generic_args, generic_train
from neuraldb.models.seq2seqargs_ret_t5cnn import Seq2seqTrainerRetT5CNN
from neuraldb.models.seq2seqargs_ret_bert import Seq2seqTrainerRetBert


class CustomEncoder(object):
    pass


def main(args):
    # If output_dir not provided, a folder will be generated in pwd
    if not args.output_dir:
        args.output_dir = os.path.join(
            "./results",
            f"{args.task}_{time.strftime('%Y%m%d_%H%M%S')}",
        )
        os.makedirs(args.output_dir)

    model = Seq2seqTrainerRetT5CNN(args)
    trainer = generic_train(model, args)

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
        model = model.load_from_checkpoint(
            checkpoints[-1],
        )
        trainer.test(model)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    add_generic_args(parser, None)

    parser = Seq2seqTrainerRetT5CNN.add_model_specific_args(parser, os.getcwd())
    args = parser.parse_args()

    main(args)
