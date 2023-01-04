#!/usr/bin/python3
"""This module contains a single function which divides all
elements of a matrix by a certain number
"""


def matrix_divided(matrix, div):
    """Divides each element of a matrix by a number `div`
    and returns a new matrix
    >>> matrix_divided([[5], [4]], 1)
    [[5.0], [4.0]]

    >>> matrix_divided([[5, 2], [3, 2]], 1.0)
    [[5.0, 2.0], [3.0, 2.0]]
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    columns = len(matrix)
    for x in matrix:
        if type(x) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    rowLength = len(matrix[0])
    for y in matrix:
        if len(y) is not rowLength:
            raise TypeError("Each row of the matrix must have the same size")

    for x in matrix:
        for elem in x:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))

    return result
