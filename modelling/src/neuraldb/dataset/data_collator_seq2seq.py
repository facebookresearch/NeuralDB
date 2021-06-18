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
from dataclasses import dataclass

import numpy as np
import torch
from typing import Optional, Union, Iterable

from transformers import PreTrainedTokenizerBase, PreTrainedModel
from transformers.file_utils import PaddingStrategy


@dataclass
class DataCollatorForSeq2SeqAllowMetadata:
    """
    Data collator that will dynamically pad the inputs received, as well as the labels.
    Args:
        tokenizer (:class:`~transformers.PreTrainedTokenizer` or :class:`~transformers.PreTrainedTokenizerFast`):
            The tokenizer used for encoding the data.
        model (:class:`~transformers.PreTrainedModel`):
            The model that is being trained. If set and has the `prepare_decoder_input_ids_from_labels`, use it to
            prepare the `decoder_input_ids`
            This is useful when using `label_smoothing` to avoid calculating loss twice.
        padding (:obj:`bool`, :obj:`str` or :class:`~transformers.file_utils.PaddingStrategy`,
        `optional`, defaults to :obj:`True`):
            Select a strategy to pad the returned sequences (according to the model's padding side and padding index)
            among:
            * :obj:`True` or :obj:`'longest'`: Pad to the longest sequence in the batch (or no padding if only a single
              sequence is provided).
            * :obj:`'max_length'`: Pad to a maximum length specified with the argument :obj:`max_length` or to the
              maximum acceptable input length for the model if that argument is not provided.
            * :obj:`False` or :obj:`'do_not_pad'` (default): No padding (i.e., can output a batch with sequences of
              different lengths).
        max_length (:obj:`int`, `optional`):
            Maximum length of the returned list and optionally padding length (see above).
        pad_to_multiple_of (:obj:`int`, `optional`):
            If set will pad the sequence to a multiple of the provided value.
            This is especially useful to enable the use of Tensor Cores on NVIDIA hardware with compute capability >=
            7.5 (Volta).
        label_pad_token_id (:obj:`int`, `optional`, defaults to -100):
            The id to use when padding the labels (-100 will be automatically ignored by PyTorch loss functions).
    """

    tokenizer: PreTrainedTokenizerBase
    model: Optional[PreTrainedModel] = None
    padding: Union[bool, str, PaddingStrategy] = True
    max_length: Optional[int] = None
    pad_to_multiple_of: Optional[int] = None
    label_pad_token_id: int = (-100,)
    metadata_field: str = "metadata"

    def __call__(self, features: Iterable[dict]):
        metadata = [
            record["metadata"] if "metadata" in record else {} for record in features
        ]

        labels = (
            [feature["labels"] for feature in features]
            if "labels" in features[0].keys()
            else None
        )
        # We have to pad the labels before calling `tokenizer.pad` as this method won't pad them and needs them of the
        # same length to return tensors.
        if labels is not None:
            max_label_length = max(len(lab) for lab in labels)
            padding_side = self.tokenizer.padding_side
            for feature in features:
                remainder = [self.label_pad_token_id] * (
                    max_label_length - len(feature["labels"])
                )
                feature["labels"] = (
                    feature["labels"] + remainder
                    if padding_side == "right"
                    else remainder + feature["labels"]
                )

        if "input_ids" in features[0]:
            master_features = self.tokenizer.pad(
                [
                    {
                        k: v
                        for k, v in feature.items()
                        if k not in {"metadata", "global_attention_mask"}
                    }
                    for feature in features
                ],
                padding=self.padding,
                max_length=self.max_length,
                pad_to_multiple_of=self.pad_to_multiple_of,
                return_tensors="pt",
            )

        if "context_ids" in features[0]:
            virtual_features = []
            lengths = []

            for feature in features:
                assert len(feature["context_ids"]) == len(feature["context_mask"])
                virtual_features.extend(
                    {
                        "input_ids": context,
                        "attention_mask": attention,
                        "labels": feature["labels"],
                    }
                    for context, attention in zip(
                        feature["context_ids"], feature["context_mask"]
                    )
                )
                lengths.append(len(feature["context_ids"]))

            master_features = self.tokenizer.pad(
                virtual_features,
                padding=self.padding,
                max_length=self.max_length,
                pad_to_multiple_of=self.pad_to_multiple_of,
                return_tensors="pt",
            )

            # master_features["lengths"] = lengths
            master_features["context_ids"] = []
            master_features["context_mask"] = []
            master_features["labels"] = torch.stack(
                [master_features["labels"][i - 1] for i in np.cumsum(lengths)], dim=0
            )

            previous = 0
            for length in lengths:
                end = previous + length

                master_features["context_ids"].append(
                    master_features["input_ids"][previous:end]
                )  # noqa: E501
                master_features["context_mask"].append(
                    master_features["attention_mask"][previous:end]
                )  # noqa: E501
                previous += length

            master_features["input_ids"] = torch.zeros((len(lengths), 1))
            del master_features["attention_mask"]

        if "global_attention_mask" in features[0]:
            additional_features = self.tokenizer.pad(
                [
                    {
                        "input_ids": feature["input_ids"],
                        "attention_mask": feature["global_attention_mask"],
                    }
                    for feature in features
                ],
                padding=self.padding,
                max_length=self.max_length,
                pad_to_multiple_of=self.pad_to_multiple_of,
                return_tensors="pt",
            )
            master_features["global_attention_mask"] = additional_features[
                "attention_mask"
            ]

        # prepare decoder_input_ids
        if (
            "labels" in master_features
            and self.model is not None
            and hasattr(self.model, "prepare_decoder_input_ids_from_labels")
        ):
            decoder_input_ids = self.model.prepare_decoder_input_ids_from_labels(
                labels=master_features["labels"]
            )
            master_features["decoder_input_ids"] = decoder_input_ids

        if any(meta for meta in metadata):
            master_features["metadata"] = metadata

        return master_features
