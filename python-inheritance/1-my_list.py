#!/usr/bin/python3
"""Define a class MyList that inherits from list"""


class MyList(list):
    """A subclass of list that provides a method to print elements sorted."""
    def print_sorted(self):
        """Prints the elements of the list in ascending order."""
        print(sorted(self))
