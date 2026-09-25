#!/usr/bin/python3
"""Module that defines a square class"""


class Square:
    """class that defines a square by its size"""

    def __init__(self, size=0):
        """Initialize a new square instance.

        Args:
            size (int): the size of the side of the square(default 0).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """calculate and return the current square area.

        Return:
            int: the area of the square(size * size)"""

        return self.__size ** 2
