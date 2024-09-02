#!/usr/bin/python3

"""This module defines a rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle class"""

    def __init__(self, width, height):
        """Initializes a rectangle object"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation"""

        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Calculate the area of a rectangle object"""
        return self.__width * self.__height
