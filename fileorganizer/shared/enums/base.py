# Base imports
from typing import List, Tuple
from enum import Enum

__all__ = [
    "BaseEnum",
]


class BaseEnum(Enum):
    """Base enumeration class with auxiliary methods."""

    @classmethod
    def choices(cls) -> List[Tuple[str]]:
        return [(item.name, item.value) for item in cls]

    @classmethod
    def values(cls) -> List[str]:
        return [item.value for item in cls]

    @classmethod
    def names(cls) -> List[str]:
        return [item.name for item in cls]
