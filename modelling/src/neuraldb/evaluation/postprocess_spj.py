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
import json
import logging
import random

import numpy as np

from neuraldb.evaluation.scoring_functions import (
    average_score,
    exact_match,
    exact_match_case_insensitive,
    breakdown_score,
)

logger = logging.getLogger(__name__)


def get_spj_evaluation(data_args, tokenizer, generator):
    def postprocess_text(preds, labels):
        preds = [
            [
                answer.strip() if len(answer.strip()) else generator.null_answer_special
                for answer in pred.replace(
                    tokenizer.bos_token if tokenizer.bos_token is not None else "", ""
                )
                .replace(
                    tokenizer.eos_token if tokenizer.eos_token is not None else "", ""
                )
                .replace(
                    tokenizer.pad_token if tokenizer.pad_token is not None else "", ""
                )
                .strip()
                .split(generator.answer_delimiter)
            ]
            for pred in preds
        ]
        labels = [
            [
                answer.strip() if len(answer.strip()) else generator.null_answer_special
                for answer in label.replace(
                    tokenizer.bos_token if tokenizer.bos_token is not None else "", ""
                )
                .replace(
                    tokenizer.eos_token if tokenizer.eos_token is not None else "", ""
                )
                .replace(
                    tokenizer.pad_token if tokenizer.pad_token is not None else "", ""
                )
                .strip()
                .split(generator.answer_delimiter)
            ]
            for label in labels
        ]

        return preds, labels

    def compute_metrics(eval_preds):
        preds, labels, metadata = eval_preds

        if isinstance(preds, tuple):
            preds = preds[0]

        decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=False)
        if data_args.ignore_pad_token_for_loss:
            # Replace -100 in the labels as we can't decode them.
            labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
        decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=False)

        # Some simple post-processing
        decoded_preds, decoded_labels = postprocess_text(decoded_preds, decoded_labels)
        if data_args.predictions_file is not None:
            with open(data_args.predictions_file, "w+") as f:
                for pred, label, meta in zip(decoded_preds, decoded_labels, metadata):
                    f.write(
                        json.dumps(
                            {"prediction": pred, "actual": label, "metadata": meta}
                        )
                        + "\n"
                    )

        sampled_ids = random.sample(list(range(len(decoded_preds))), 10)
        for id in sampled_ids:
            logger.info(
                f"Example prediction  \n"
                f"Q: {metadata[id]['question']}\n"
                f"P: {decoded_preds[id]}\n"
                f"A: {decoded_labels[id]}\n"
                f"\n"
            )

        em = average_score(decoded_labels, decoded_preds, exact_match)
        em_lower = average_score(
            decoded_labels, decoded_preds, exact_match_case_insensitive
        )

        result = {
            "em": em,
            "emi": em_lower,
            "em_breakdown_type": breakdown_score(
                "type", decoded_labels, decoded_preds, metadata, exact_match
            ),
            "em_breakdown_relation": breakdown_score(
                "relation", decoded_labels, decoded_preds, metadata, exact_match
            ),
        }

        prediction_lens = [
            np.count_nonzero(pred != tokenizer.pad_token_id) for pred in preds
        ]
        result["gen_len"] = np.mean(prediction_lens)
        result = {
            k: {k2: round(v2, 4) for k2, v2 in v.items()}
            if isinstance(v, dict)
            else round(v, 4)
            for k, v in result.items()
        }
        return result

    return compute_metrics
