#!/usr/bin/python3

"""This module defines a rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle class"""

    def __init__(self, width, height):
        """Initializes a rectangle object"""

        super().__init__()

        if self.integer_validator("width", width):
            self.__width = width

        if self.integer_validator("height", height):
            self.__height = height
