from dataclasses import dataclass
from typing import Optional, List, Any


@dataclass(frozen=True)
class NewClassificationExample:
    """
    A single commands/test example for NeuralDB

    Args:
        tokens
        label: (Optional) string. The label of the example. This should be
            specified for train and dev examples, but not for test examples.
        metadata
    """

    token_ids: List[int]
    label_idx: Optional[int]
    metadata: Optional[Any]


@dataclass(frozen=True)
class PaddedClassificationFeatures:
    """
    A single commands/test example for NeuralDB

    Args:
        tokens
        label: (Optional) string. The label of the example. This should be
            specified for train and dev examples, but not for test examples.
        metadata
    """

    input_ids: List[int]
    token_type_ids: List[int]
    attention_mask: List[int]
    label: Optional[int]
