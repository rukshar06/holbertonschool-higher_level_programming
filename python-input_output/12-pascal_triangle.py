#!/usr/bin/python3
"""Module that returns a list of lists of integers
representing the Pascal's triangle of n"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Initialize a row of size (i + 1) filled with 1s
        row = [1] * (i + 1)

        # Calculate intermediate values using the previous row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
