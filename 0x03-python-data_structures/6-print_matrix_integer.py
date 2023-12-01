#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""

    if matrix == [[]]:
        print("")
    else:
        for row in matrix:
            for cell in row:
                if row.index(cell) == len(row) - 1:
                    print("{:d}".format(cell))
                else:
                    print("{:d} ".format(cell), end="")
