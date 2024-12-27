# Base imports
from typing import Any, Generator, Tuple

__all__ = [
    "is_empty_no_side_effects",
]


type TGenerator = Generator[Any, None, None]


def is_empty_no_side_effects(
    generator: Generator[Any, None, None]
) -> Tuple[Generator[Any, None, None], bool]:
    """Checks is a generator is empty. If we are not suppose to consume any
    item then we need to re-inject the first item into the generator."""
    try:
        item = next(generator)

        def my_generator() -> TGenerator:
            yield item
            yield from generator

        return my_generator(), False
    except StopIteration:
        return (_ for _ in []), True
