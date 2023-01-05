#!/usr/bin/python3
"""This is a python module that defines a single
class that defines a rectangle"""


class Rectangle:
    """This is a class that defines a rectangle

    Attributes:
        width(int): The width of the rectangle
        height(int): The height of the rectangle

        >>> my_rect = Rectangle(3, 5)
        >>> my_rect.width
        3
        >>> my_rect.height
        5
        >>> my_rect.width = 6
        >>> my_rect.height = 10
        >>> my_rect.width
        6
        >>> my_rect.height
        10

    Height and Width must be integers
    ::
        >>> my_rect.width = "w"
        Traceback (most recent call last):
            ...
        TypeError: width must be an integer

        >>> my_rect.height = "h"
        Traceback (most recent call last):
            ...
        TypeError: height must be an integer

        >>> my_rect = Rectangle(3, "h")
        Traceback (most recent call last):
            ...
        TypeError: height must be an integer

        >>> my_rect = Rectangle("w", 6)
        Traceback (most recent call last):
            ...
        TypeError: width must be an integer

    Height and width must not be less than 0
    ::
        >>> my_rect.width = -4
        Traceback (most recent call last):
            ...
        ValueError: width must be >= 0

        >>> my_rect.height = -8
        Traceback (most recent call last):
            ...
        ValueError: height must be >= 0

        >>> my_rect = Rectangle(3, -4)
        Traceback (most recent call last):
            ...
        ValueError: height must be >= 0

        >>> my_rect = Rectangle(-2, 5)
        Traceback (most recent call last):
            ...
        ValueError: width must be >= 0
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
