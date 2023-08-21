# Base imports
from typing import Any, Generator, Tuple


def is_empty_no_side_effects(generator: Generator[Any, None, None]) -> Tuple[Generator[Any, None, None], bool]:
    """Checks is a generator is empty. If we are not suppose to consume any
    item then we need to re-inject the first item into the generator."""
    try:
        item = next(generator)
        
        def my_generator():
            yield item
            yield from generator
        
        return my_generator(), False
    except StopIteration:
        return (_ for _ in []), True
