#!/usr/bin/python3
"""Module that contains a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number to divide all matrix elements by.

    Returns:
        list: A new matrix with the results of the division.
        """

    # validate 'div' parameter first#
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 2. Validate 'matrix' standard structure#
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    row_len = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)

        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for x in row:
            if not isinstance(x, (int, float)) or isinstance(x, bool):
                raise TypeError(msg)

    # 3. Divide and construct new matrix
    return [[round(x / div, 2) for x in row] for row in matrix]
