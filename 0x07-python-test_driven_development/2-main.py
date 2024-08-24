#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [40, 2, 3],
    [4, 24, 6]
]
print(matrix_divided(matrix, float('inf')))
print(matrix)
