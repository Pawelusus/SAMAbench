"""Optimizer base class"""

from abc import ABC, abstractmethod

import numpy as np

from samabench.base.types import FloatArray, SearchSpace


class Optimizer(ABC):
    """Base optimizer (metaheuristic) class

    Internal state (population, velocities, covariance matrix...) lives as attributes
    of the instance.
    """

    def __init__(self, space: SearchSpace, rng: np.random.Generator) -> None:
        """Initializes the optimizer.

        Args:
            space: Search space object
            rng: Random number generator
        """
        self.space = space
        self.rng = rng

    @abstractmethod
    def ask(self, n: int) -> FloatArray:
        """Returns ``n`` new generated candidates.

        Args:
            n: Number of candidates to return

        Returns:
            FloatArray: New candidates, shape ``(n, dims)``
        """
        # TODO: check if this is good enough - not all optimizers
        # allow asking for specified amount of candidates (cma)

    @abstractmethod
    def tell(self, X: FloatArray, y: FloatArray) -> None:
        """Updates the internal state with the results.

        Args:
            X: Points in search space; shape ``(n, dims)``
            y: Values for each point; shape ``(n,)``
        """
        # TODO: check if this is good enough - some optimizers
        # need more info (de, pso need info wich element this refers to)

    @abstractmethod
    def best(self) -> tuple[FloatArray, float]:
        """Returns the best found point (``x``,, ``y``)

        Returns:
            tuple[FloatArray, float]: The best point ``x`` and its value ``y``.
        """
