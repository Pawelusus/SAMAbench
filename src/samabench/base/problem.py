"""Problem base class"""

from abc import ABC, abstractmethod
from typing import Literal

from samabench.base.types import Bounds, FloatArray, SearchSpace, VariableType


class Problem(ABC):
    """Base problem class"""

    @abstractmethod
    def evaluate(self, x: FloatArray) -> float:
        """Returns value of function in point x

        Args:
            x: point to evaluate of shape ``(dims(),)``

        Returns:
            function value in point ``x``
        """

    @abstractmethod
    def get_bounds(self) -> Bounds:
        """Get problem bounds
        Returns:
            Bounds: upper and lower bounds
        """

    @abstractmethod
    def get_var_types(self) -> list[VariableType]:
        """Get list of variables types per dimension
        Returns:
            list[VariableType]: type per dimension; shape ``dims()``
        """

    @abstractmethod
    def get_dims(self) -> int:
        """Get problem dimension
        Returns:
            int: dimension of the search space
        """

    def get_search_space(self) -> SearchSpace:
        """
        Returns:
            SearchSpace: info about bounds and variable types
        """

        return SearchSpace(bounds=self.get_bounds(), vartypes=self.get_var_types())

    def get_cost_class(self) -> Literal["cheap", "expensive"]:
        """Problem evaluation cost, ``expensive`` by deafult

        Syntethic, BBOB -> cheap

        Engineering -> expensive

        Returns:
            Literal["cheap", "expensive"]: cost class
        """
        return "expensive"
