#!/usr/bin/python3

"""Declares a Geometry class"""


class BaseGeometry:
    """Initializes a Geometry class"""

    def area(self):
        """Define an area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Defines an integer validator"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
