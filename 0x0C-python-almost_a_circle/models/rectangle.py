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

    @staticmethod
    def is_integer(attr_name, attr_value):
        """Checks if a value is an integer"""
        if type(attr_value) is not int:
            raise TypeError(f"{attr_name} must be an integer")

    @staticmethod
    def is_natural_number(attr_name, attr_value):
        """Checks if a number is > 0"""
        if attr_value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    @staticmethod
    def is_not_negative(attr_name, attr_value):
        """Checks if a number is >= 0"""
        if attr_value < 0:
            raise ValueError(f"{attr_name} must be >= 0")

    def area(self):
        """Calculates the area of the rectangle object"""

        return self.__width * self.__height

    def display(self):
        """Print the rectangle using the '#' character"""

        for a in range(self.__y):
            print()
        for i in range(self.__height):
            for b in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a printable string representation"""

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Updates the rectangle"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            try:
                for k, v in kwargs.items():
                    setattr(self, k, v)
            except Exception as e:
                print(e)
