#!/usr/bin/python3

from abc import ABC, abstractmethod


class shape(ABC):
    """An abstract base class representing a shape."""

    @abstractmethod
    def area(self):
        """calculate and return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """calculate and return the perimeter of the shape."""
        pass


class circle(shape):
    """concrete class representing a circle, inheriting from shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle, inheriting from Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Accepts any object and prints its area and perimeter
    relying entirely on duck typing (no isinstance checks).
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
