#!/usr/bin/python3
"""a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of, or inherited from,
    a specified class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is an instance of or inherited from a_class,
        otherwise False.
    """
    return isinstance(obj, a_class)
