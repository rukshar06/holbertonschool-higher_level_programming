#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited

    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj inherited from a_class (and is not an exact instance
        of a_class itself), otherwise False.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
