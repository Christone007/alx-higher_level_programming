#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    breadth = len(matrix[0])
    for i in range(length):
        if breadth == 0:
            print()
            return
        for j in range(breadth):
            if j == breadth - 1:
                print("{}".format(matrix[i][j]))
            else:
                print("{}".format(matrix[i][j]), end=" ")
