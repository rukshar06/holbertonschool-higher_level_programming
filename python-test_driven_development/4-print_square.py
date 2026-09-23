#!/usr/bin/python3
"""Define a function that prints a square with the character #.
"""


def print_square(size):
    """This function prints a square with char #
    if it's not an int it raises a TypeError
    if it's less than zero and a float it raises
    ValueError and TypeError
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if (size) < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
