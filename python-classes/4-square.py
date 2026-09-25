#!/usr/bin/python3
"""Module that defines a square class"""


class Square:
    """class that defines a square by its size"""

    def __init__(self, size=0):
        """Initialize a new square instance.

        Args:
            size (int): the size of the size of the square(default 0).
        """
        self.size = size

    @property
    def size(self):
        """get the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        args:
            value (int): the new size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
