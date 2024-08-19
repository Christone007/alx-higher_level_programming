#!/usr/bin/python3

"""The Square Module

This module documents a class that simply creates a square

"""


class Square:
    """This class defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square

        Args:
            size: The length of the square
            position: The cordinates of the square's position
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """The size getter property"""
        return self.__size

    @property
    def position(self):
        """The position getter property"""
        return self.__position

    @size.setter
    def size(self, size):
        """The size setter"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @position.setter
    def position(self, value):
        if not (
                isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(x, int) and x >= 0 for x in value)
                ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character
        Also prints the square from correct
        position in space ignoring the y axis
        """
        if self.__size == 0:
            print()
        else:
            for l in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
