#!/usr/bin/python3

"""Define a Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square"""

    def __init__(self, size):
        """Initialize the Square object"""

        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Returns the area of the square object"""

        return self.__size ** 2

    def __str__(self):
        """Returns a string format"""
        return f"[Square] {self.__size}/{self.__size}"
