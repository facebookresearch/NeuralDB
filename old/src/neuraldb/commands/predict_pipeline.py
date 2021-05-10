import json
from argparse import ArgumentParser
from copy import deepcopy
from operator import itemgetter
import numpy as np
import torch
from sklearn.metrics import recall_score, precision_score
from tqdm import tqdm

from neuraldb.dataset.base_reader import NeuralDatabaseDatasetReader
from neuraldb.dataset.e2e_reader.v0_5_database_reader import V5DatabaseSpecificReader
from neuraldb.dataset.instance_generator import InstanceGenerator
from neuraldb.demo.helpers import (
    load_cls_model,
    cls_forward,
    nuo_forward,
    load_nuo_model,
)
from neuraldb.models.cls_operator import CLSTransformer
from neuraldb.models.operator_run import RunSeq2seqOperatorTrainer


if __name__ == "__main__":
    parser = ArgumentParser(conflict_handler="resolve")
    CLSTransformer.add_model_specific_args(parser, None)
    RunSeq2seqOperatorTrainer.add_model_specific_args(parser, None)
    parser.add_argument("--cls_model", required=True)
    parser.add_argument("--nuo_model", required=True)
    parser.add_argument("--in_file", required=True)
    parser.add_argument("--out_file", required=True)
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    cls_model = load_cls_model(args)
    nuo_model = load_nuo_model(args)
    nuo_model.eval().to(device)

    with open(args.in_file) as f:
        databases = json.load(f)

    reader = V5DatabaseSpecificReader(max_list_len=None)

    with open(args.out_file, "w+") as out_file:
        for db_idx, database in tqdm(enumerate(databases), desc="Reading databases"):
            db = reader.load_instances(databases[0])
            facts = list(map(itemgetter("text"), db["updates"]))

            for query in tqdm(db["queries"], "Local query"):
                action = cls_forward(cls_model, query["input"])
                projected = nuo_forward(
                    nuo_model, facts[: query["context_height"]], query["input"], device
                )
                projected_ids = [
                    idx
                    for idx, a in enumerate(projected)
                    if a != InstanceGenerator.null_answer_special
                ]
                query["output_type"] = str(query["output_type"])
                query["metadata"]["output_type"] = str(query["metadata"]["output_type"])
                out_file.write(
                    json.dumps(
                        {
                            "database": db_idx,
                            "query": query,
                            "projected": projected,
                            "projected_ids": projected_ids,
                            "action": action,
                        }
                    )
                    + "\n"
                )
