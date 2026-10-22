#!/usr/bin/python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """An abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """A Dog subclass of Animal."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """A Cat subclass of Animal."""

    def sound(self):
        return "Meow"