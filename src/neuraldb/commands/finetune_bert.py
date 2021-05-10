import argparse
import glob
import logging
import os
import time

from lightning_base import add_generic_args, generic_train
from neuraldb.models.cls_operator import CLSTransformer

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    add_generic_args(parser, os.getcwd())
    parser = CLSTransformer.add_model_specific_args(parser, os.getcwd())
    args = parser.parse_args()

    # If output_dir not provided, a folder will be generated in pwd
    if args.output_dir is None:
        args.output_dir = os.path.join(
            "./results",
            f"{args.task}_{time.strftime('%Y%m%d_%H%M%S')}",
        )
        os.makedirs(args.output_dir)

    model = CLSTransformer(args)
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
        model = model.load_from_checkpoint(checkpoints[-1])
        trainer.test(model)
