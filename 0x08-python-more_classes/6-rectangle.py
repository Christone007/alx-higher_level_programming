#!/usr/bin/python3

"""This module defines a rectangle class
"""


class Rectangle:
    """This class defines a rectangle class

    Description: Defines a rectangle

    Instance attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Prints the rectangle using #"""

        if self.__width == 0 or self.__height == 0:
            return ""

        rect = ""

        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            if i < self.__height - 1:
                rect += "\n"

        return rect

    def __repr__(self):
        """Returns a string representation of the object"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
