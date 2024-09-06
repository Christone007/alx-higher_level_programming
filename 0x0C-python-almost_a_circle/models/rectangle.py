#!/usr/bin/python3

"""
The Rectangle Module
"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle object"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # Call the parent class
        super().__init__(id)

    # Setters and getters
    @property
    def width(self):
        """Gets the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        try:
            self.is_integer("width", value)
            self.is_natural_number("width", value)
        except Exception as e:
            raise e

        self.__width = value

    @property
    def height(self):
        """Gets the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        try:
            self.is_integer("height", value)
            self.is_natural_number("height", value)
        except Exception as e:
            raise e

        self.__height = value

    @property
    def x(self):
        """Fetches the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x attribute"""
        try:
            self.is_integer("x", value)
            self.is_not_negative("x", value)
        except Exception as e:
            raise e

        self.__x = value

    @property
    def y(self):
        """Fetches the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y attribute"""
        try:
            self.is_integer("y", value)
            self.is_not_negative("y", value)
        except Exception as e:
            raise e

        self.__y = value

    def is_integer(self, attr_name, attr_value):
        """Checks if a value is an integer"""
        if type(attr_value) is not int:
            raise TypeError(f"{attr_name} must be an integer")

    def is_natural_number(self, attr_name, attr_value):
        """Checks if a number is > 0"""
        if attr_value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    def is_not_negative(self, attr_name, attr_value):
        """Checks if a number is >= 0"""
        if attr_value < 0:
            raise ValueError(f"{attr_name} must be >= 0")

    def area(self):
        """Calculates the area of the rectangle object"""

        return self.__width * self.__height
