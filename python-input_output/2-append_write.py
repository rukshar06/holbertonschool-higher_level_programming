#!/usr/bin/python3
"""Module for appending a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string to a text file
    and returns the number of char"""

    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
