#!/usr/bin/python3

"""The Square Module

This module documents a class that simply creates a square

"""


class Square:
    """This class defines a square
    """

    def __init__(self, size=0):
        """Initializes the square

        Args:
            size: The length of the square
        """

        self.size = size

    @property
    def size(self):
        """The getter function"""
        return self.__size

    @size.setter
    def size(self, size=0):
        """The size setter"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2
