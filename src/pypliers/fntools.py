"""A collection of Higher Order Functions."""
from typing import Any, Callable, Tuple, TypeVar, Union

T = TypeVar("T")
U = TypeVar("U")


def if_fn(cond: bool, do_true: Tuple[Callable[..., T], ...], do_false: Tuple[Callable[..., U], ...]) -> Union[T, U]:
    """Execute a specific expression along with the arguments to pass to it depending on a condition.

    Args:
        cond (bool): condition to evaluate
        do_true (Tuple[Callable[..., T], ...]): A tuple with expression to execute as head along with a
                                                tail of arguments if the condition is truthy
        do_false (Tuple[Callable[..., U], ...]): A tuple with expression to execute as head along with a
                                                 tail of arguments if the condition is falsey

    Returns
    -------
        Union[T, U]: The result of the expression that was executed
    """
    if cond:
        return do_true[0](*do_true[1:])
    return do_false[0](*do_true[1:])


def interpret(structure: Tuple) -> Any:
    """Interpret a tuple as a function and its arguments. Micro lisp interpreter.

    Args:
        structure (Tuple): A tuple with a function as head and a tail of arguments

    Returns
    -------
        Callable: A function
    """
    return structure[0](*(interpret(i) if isinstance(i, tuple) and callable(i[0] if len(i) > 0 else None) else i for i in structure[1:]))
