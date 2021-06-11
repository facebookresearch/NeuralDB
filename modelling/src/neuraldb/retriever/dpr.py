import json
import logging

import torch
from argparse import ArgumentParser
from tqdm import tqdm
from transformers import (
    DPRContextEncoderTokenizer,
    DPRContextEncoder,
)
from transformers import DPRQuestionEncoder, DPRQuestionEncoderTokenizer

from neuraldb.util.log_helper import setup_logging

logger = logging.getLogger(__name__)


class DPRRetriever:
    def __init__(self):
        self.question_tokenizer = DPRQuestionEncoderTokenizer.from_pretrained(
            "facebook/dpr-question_encoder-single-nq-base"
        )
        self.question_model = DPRQuestionEncoder.from_pretrained(
            "facebook/dpr-question_encoder-single-nq-base"
        ).to("cuda")
        self.context_tokenizer = DPRContextEncoderTokenizer.from_pretrained(
            "facebook/dpr-ctx_encoder-single-nq-base"
        )
        self.context_model = DPRContextEncoder.from_pretrained(
            "facebook/dpr-ctx_encoder-single-nq-base"
        ).to("cuda")

    def lookup(self, queries, facts):
        encoded_questions = self.question_tokenizer(queries, padding=True)
        device_inputs = {
            k: torch.LongTensor(v).to("cuda") for k, v in encoded_questions.items()
        }
        question_outputs = self.question_model(**device_inputs)

        encoded_context = self.context_tokenizer(facts, padding=True)
        device_inputs = {
            k: torch.LongTensor(v).to("cuda") for k, v in encoded_context.items()
        }
        context_outputs = self.context_model(**device_inputs)

        yield from torch.matmul(
            question_outputs.pooler_output, context_outputs.pooler_output.T
        ).cpu().detach().numpy().argsort(axis=1).tolist()


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    args = parser.parse_args()

    setup_logging()
    dpr = DPRRetriever()
    dpr.context_model.eval()
    dpr.question_model.eval()
    with open(args.in_file) as f, open(args.out_file, "w+") as of:
        for line in tqdm(f):
            database = json.loads(line)

            facts = database["facts"]
            queries = [q["query"] for q in database["queries"]]

            for query, ids in zip(database["queries"], dpr.lookup(queries, facts)):
                filtered_ids = list(
                    filter(lambda idx: idx <= query["height"], ids[::-1])
                )
                query["predicted_facts"] = [filtered_ids]

            of.write(json.dumps(database) + "\n")
