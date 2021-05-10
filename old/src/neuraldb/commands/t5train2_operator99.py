import argparse
import glob

import os
from datetime import time
from pathlib import Path

from lightning_base import add_generic_args, generic_train
from neuraldb.models.seq2seqargs_operator99 import Seq2seqOperatorTrainer99


def main(args):
    # If output_dir not provided, a folder will be generated in pwd
    if not args.output_dir:
        args.output_dir = os.path.join(
            "./results",
            f"{args.task}_{time.strftime('%Y%m%d_%H%M%S')}",
        )
        os.makedirs(args.output_dir)

    model = Seq2seqOperatorTrainer99(args)
    trainer = generic_train(model, args)

    if args.do_predict:
        print(os.path.exists(args.output_dir))
        model = model.load_from_checkpoint(
            args.output_dir + "/best_em.ckpt",
            test_path=args.test_path,
            external_test=True,
        )

        model.test_metrics_save_path = Path(model.output_dir) / args.test_name
        trainer.test(model)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    add_generic_args(parser, None)
    parser = Seq2seqOperatorTrainer99.add_model_specific_args(parser, os.getcwd())
    args = parser.parse_args()

    main(args)
