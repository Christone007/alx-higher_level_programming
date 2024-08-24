#!/usr/bin/python3

"""This is a module that defines a function that prints a square
"""


def print_square(size):
    """Prints a square

    Args:
        size(int): The length of the square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
