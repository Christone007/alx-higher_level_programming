#!/usr/bin/python3

"""The Square Module

This module documents a class that simply creates a square

"""


class Square:
    """This class defines a square
    """

    def __init__(self, size):
        """Initializes the square

        Args:
            size: The length of the square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
