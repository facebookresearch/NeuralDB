import argparse
import glob
import json
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
    NeuralDatabaseDatasetSingleReader,
)
from neuraldb.dataset.e2e_generator.seq2seq_reader import Seq2SeqSpecificGenerator
from neuraldb.dataset.e2e_generator.surrogate_test import (
    Seq2SeqSpecificSurrogateGenerator,
)
from neuraldb.dataset.e2e_generator.surrogate_test_non_generator import (
    Seq2SeqSpecificSurrogateReader,
)
from neuraldb.dataset.e2e_reader.v0_5_database_reader import V5DatabaseSpecificReader
from neuraldb.dataset.generic_dataset import GenericDataset, AutoLoadDataset
from neuraldb.dataset.search_engines.return_all import ReturnAll
from neuraldb.models.seq2seqargs import Seq2seqTrainer

logger = logging.getLogger(__name__)


def get_dataset_reader():
    return V5DatabaseSpecificReader(
        max_queries=None, max_list_len=None, filter_types=None
    )


def construct_generator(surrogate):
    def fwd(instances):

        loader = DataLoader(
            [surrogate.data_generator.pad(i) for i in instances],
            batch_size=32,
            collate_fn=surrogate.data_generator.collate_fn,
        )

        projected = []
        with torch.no_grad():
            for batch in loader:
                batch = {
                    k: v.to("cuda") if isinstance(v, torch.Tensor) else v
                    for k, v in batch.items()
                }
                projected.extend(
                    surrogate.model.generate(
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
                        bad_words_ids=surrogate.bad_words,
                    )
                )

        return [
            surrogate.data_generator._tokenizer.decode(p, skip_special_tokens=True)
            for p in projected
        ]

    return Seq2SeqSpecificSurrogateReader(surrogate, fwd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--surrogate", required=True, type=str)
    parser.add_argument("--db", required=True, type=int)
    parser.add_argument("--file", required=True, type=str)
    parser.add_argument("--out", required=True, type=str)

    args = parser.parse_args()
    surrogate = Seq2seqTrainer.load_from_checkpoint(args.surrogate + "/best_em.ckpt")
    surrogate.data_generator.test_mode = True
    surrogate = surrogate.to("cuda")

    data_reader = get_dataset_reader()
    data_generator = construct_generator(surrogate)
    reader = NeuralDatabaseDatasetSingleReader(data_reader, data_generator, args.db)

    with open(args.out, "w+") as of:
        for a in reader.read(args.file):
            of.write(json.dumps(a, default=str) + "\n")
