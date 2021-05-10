from dataclasses import dataclass
from typing import Optional, List, Any, Dict


@dataclass(frozen=True)
class MultiGenerationExample:
    """
    A single commands/test example for NeuralDB

    Args:
        tokens
        label: (Optional) string. The label of the example. This should be
            specified for train and dev examples, but not for test examples.
        metadata
    """

    token_ids: List[int]
    context_ids: List[List[int]]
    label_ids: Optional[List[int]]
    label_toks: Optional[List[str]]
    metadata: Optional[Dict[str, Any]]


@dataclass(frozen=True)
class PaddedMultiGenerationFeatures:
    """
    A single commands/test example for NeuralDB

    Args:
        tokens
        label: (Optional) string. The label of the example. This should be
            specified for train and dev examples, but not for test examples.
        metadata
    """

    input_ids: List[int]
    attention_mask: List[int]
    context_ids: List[List[int]]
    context_mask: List[List[int]]
    decoder_input_ids: Optional[List[int]]
    lm_labels: Optional[List[int]]
    metadata: Optional[List[Dict[str, Any]]]
