#!/usr/bin/python3

"""This module contains a function that multiplies
matrices
"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices

    Args:
        m_a: The first matrix
        m_b: The second matrix

    Returns:
        The product of the 2 matrices
    """

    #variables
    rows_a = 0
    rows_b = 0
    cols_a = 0
    cols_b = 0

    #prelimary validation of both matrices
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
   
    #validate matrix a
    if len(m_a) > 0:
       if type(m_a[0]) is not list:
           raise TypeError("m_a must be a list of lists")
       if len(m_a) == 1 and len(m_a[0]) == 0:
           raise ValueError("m_a can't be empty")
       cols_a = len(m_a[0])

    for row_a in m_a:
        if type(row_a) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(row_a) != cols_a:
            raise TypeError("each row of m_a must be of the same size")
        for elem_a in row_a:
            if type(elem_a) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
        rows_a += 1

    #validate matrix b
    if len(m_b) > 0:
        if type(m_b[0]) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(m_b) == 1 and len(m_b[0]) == 0:
            raise ValueError("m_b can't be empty")
        cols_b = len(m_b[0])

    for row_b in m_b:
        if type(row_b) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(row_b) != cols_b:
            raise TypeError("each row of m_b must be of the same size")
        for elem_b in row_b:
            if type(elem_b) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")
        rows_b += 1

    #check if both matrices can be multiplied
    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    #multiply matrices
    matrix = []
    
    for i in range(rows_a):
        result = []
        for j in range(cols_b):
            prod = 0
            for k in range(cols_a):
                prod += m_a[i][k] * m_b[k][j]
            result.append(round(prod, 2))
        matrix.append(result)

    return matrix
