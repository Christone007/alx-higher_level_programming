#!/usr/bin/python3

"""This Module prints a pascal's triangle"""


def pascal_triangle(n):
    """Prints a pascal's triangle of size n"""

    if n <= 0:
        return []

    prev = []
    triangle = []

    for i in range(n):
        my_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                my_list.append(1)
            else:
                my_list.append(prev[j - 1] + prev[j])
        prev = my_list
        triangle.append(my_list)

    return triangle
