#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Squares all elements of a matrix"""
    if matrix == []:
        return []

    result = []
    for row in matrix:
        result.append(list(map(lambda x:x**2, row)))
    return result
