"""A collection of functions for working with dictionaries."""
from collections.abc import Callable, Iterator
from typing import Any


def get(d: dict, key: str, default: Any = None) -> Any:
    """Return value from a dictionary based on a key.

    Args:
        d (dict): A dictionary
        key (str): A key
        default (Any, optional): Default return if key is not found. Defaults to None.

    Returns
    -------
        Any: A value at key or default
    """
    return d.get(key, default)


def get_in(d: dict, keys: list, default: Any = None) -> Any:
    """Return a value from a nested dictionary based on a list of keys.

    Args:
        d (dict): A dictionary
        keys (list): A list of keys
        default (Any, optional): Default return if keys are not found. Defaults to None.

    Returns
    -------
        Any: A value at nested key or default
    """
    if len(keys) == 0:
        return d
    key = keys[0]
    return get_in(get(d, key, default), keys[1:], default)


def assoc(d: dict, key: Any, value: Any) -> dict:
    """Place value at the key in a dictionary.

    Args:
        d (dict): A dictionary
        key (Any): A key
        value (Any): A value to place at key

    Returns
    -------
        dict: Dictionary modified with key and value
    """
    return {**d, key: value}


def assoc_in(d: dict, keys: list, value: Any) -> Any:
    """Place value at in a nested dictionary based on a list of keys.

    Args:
        d (dict): A dictionary
        keys (Any): A list of keys
        value (Any): A value to place at the nested key

    Returns
    -------
        dict: Dictionary modified with key and value
    """
    if len(keys) == 0:
        return value

    key = keys[0]
    return assoc(d, key, assoc_in(get(d, key, {}), keys[1:], value))


def dissoc(d: dict, key: str) -> dict:
    """Remove a key from a dictionary.

    Args:
        d (dict): A dictionary
        key (str): A key

    Returns
    -------
        dict: A dictionary modified with key removed
    """
    return {k: v for k, v in d.items() if k != key}


def dissoc_in(d: dict, keys: list) -> Any:
    """Remove a key from a dictionary.

    Args:
        d (dict): A dictionary
        keys (str): A list of keys

    Returns
    -------
        dict: A dictionary modified with nested key removed
    """
    if len(keys) == 0:
        return d  # pragma: no cover
    return assoc_in(d, keys[:-1], dissoc(get_in(d, keys[:-1]), keys[-1]))


def __flatten_dict(d: dict, parent_keys: list) -> Iterator:
    for key, value in d.items():
        keys = [*parent_keys, key]
        if isinstance(value, dict):
            yield from __flatten_dict(value, keys)
        else:
            yield (keys, value)


def flatten_dict(d: dict) -> Iterator[tuple[list[Any], Any]]:
    """Flatten a dictionary into an iterator of tuples containing a list of keys and a value.

    Args:
        d (dict): A dictionary

    Yields
    ------
        Iterator[Tuple[List[Any], Any]]: Iterator of tuples containing a list of keys and a value
    """
    parent_keys: list = []
    return __flatten_dict(d, parent_keys)


def walk_deep(f: Callable, d: dict, walk_keys: bool = False) -> dict:
    """Walk a dictionary and apply a function to each value or key depending on walk_keys.

    Args:
        f (Callable): A function to apply to each value or key
        d (dict): A dictionary
        walk_keys (bool, optional): A flag configuring whether to apply to key or value. Defaults to False.

    Returns
    -------
        dict: A dictionary with function applied to each value or key
    """
    if walk_keys:
        return {f(key): walk_deep(f, value, True) if isinstance(value, dict) else value for key, value in d.items()}

    return {key: walk_deep(f, value, False) if isinstance(value, dict) else f(value) for key, value in d.items()}
