#!/usr/bin/python3

"""This module divides a list of lists of integers/floats
It contains only one function
"""


def matrix_divided(matrix, div):
    """This function divides a matrix by a given number

    Args:
        matrix: A list of lists of integers/floats
        div: A number to dividde each of elements of the matrix

    Returns:
        Returns a list of lists of floats rounded to 2 decimal places
    """

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = 0
    result = []

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
    if len(matrix) > 0:
        if type(matrix[0]) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
        row_length = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
        try:
            new_row = [round(x/div, 2) for x in row]
        except ZeroDivisionError:
            raise ZeroDivisionError("division by zero")
        else:
            result.append(new_row)

    return result
