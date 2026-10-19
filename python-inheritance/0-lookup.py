#!/usr/bin/python3
"""Defines an object attribute lookup function"""


def lookup(obj):
    """Returns a list of available attributes and methods."""
    # Get all attributes and methods of the object

    my_list = dir(obj)
    return (dir(obj))
