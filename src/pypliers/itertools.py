"""A collection of functions for working with iterables."""
from collections.abc import Callable, Generator, Iterable
from typing import Any, TypeVar

# TODO: Add tests for these functions

T = TypeVar("T")


def flatten(coll: Iterable) -> Generator[Any, None, None]:
    """Flatten an iterable of iterables.

    Args:
        coll (Iterable): Iterable of iterables to flatten

    Yields
    ------
        Generator: A generator of flattened elements
    """
    for el in coll:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


def flatmap(f: Callable[..., T], coll: Iterable) -> Generator[T, None, None]:
    """Map a function over an iterable and flatten the result.

    Args:
        f (Callable): A function to map over an iterable
        coll (Iterable): An iterable to map over

    Yields
    ------
        Generator: A generator of flattened elements
    """
    return flatten(map(f, coll))
