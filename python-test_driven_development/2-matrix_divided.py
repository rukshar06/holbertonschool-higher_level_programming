#!/usr/bin/python3
"""Module that contains a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix"""

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 2. Validate 'matrix' standard structure
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(msg)

    row_len = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg)

        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError(msg)

    # 3. Divide and construct new matrix
    return [[round(x / div, 2) for x in row] for row in matrix]
