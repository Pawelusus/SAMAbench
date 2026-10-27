"""Common types and data structures"""

from dataclasses import dataclass
from enum import StrEnum

import numpy as np
from numpy.typing import NDArray

type FloatArray = NDArray[np.float64]


class VariableType(StrEnum):
    """Type of variable"""

    CONTINUOUS = "cont"
    INTEGER = "int"
    CATEGORICAL = "cat"


@dataclass(frozen=True)
class Bounds:
    """Lower and upper bounds"""

    lower: FloatArray
    upper: FloatArray

    def __post_init__(self) -> None:
        """Enforce same shape of ``lower`` and ``upper``"""
        if self.lower.shape != self.upper.shape:
            raise ValueError("lower and upper shape is required to match")


@dataclass(frozen=True)
class SearchSpace:
    """Full searchspace specyfication"""

    bounds: Bounds
    vartypes: list[VariableType]
