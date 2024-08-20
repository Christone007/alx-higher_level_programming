#!/usr/bin/python3

import math

"""Translated manually from pytgon bytecode"""


class MagicClass:
    """The magic class"""

    def __init__(self, radius):
        self.__radius = 0
        if (
                type(radius) is not int and
                type(radius) is not float
                ):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the circle"""

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the circle"""
        return math.pi * 2 * self.__radius
