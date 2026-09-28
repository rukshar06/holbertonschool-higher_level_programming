#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Defines a square with size and position attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int): The side length of the square (default 0).
            position (tuple): The (x, y) coordinates for offset (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with type and value validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with type and value validation."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(type(i) is int for i in value)
            or not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' taking position offset into account."""
        if self.__size == 0:
            print()
            return

        # Print vertical space (position[1])#
        for _ in range(self.__position[1]):
            print()

        # Print horizontal space (position[0]) and '#' characters
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
