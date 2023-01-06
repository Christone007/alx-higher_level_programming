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

        >>> my_rect = Rectangle(3, 4)
        >>> my_rect.area()
        12
        >>> my_rect.perimeter()
        14

        >>> my_rect = Rectangle(0, 3)
        >>> my_rect.area()
        0
        >>> my_rect.perimeter()
        0

        >>> my_rect = Rectangle(3, 5)
        >>> print(my_rect)
        ###
        ###
        ###
        ###
        ###

        >>> my_rect = Rectangle(2, 3)
        >>> print(str(my_rect))
        ##
        ##
        ##

        >>> print(Rectangle(0, 5))
        <BLANKLINE>
        >>> print(Rectangle(5, 0))
        <BLANKLINE>
        >>> print(Rectangle(0, 0))
        <BLANKLINE>

        >>> my_rect = Rectangle(2, 3)
        >>> new_rect = eval(repr(my_rect))
        >>> print(repr(new_rect))
        Rectangle(2, 3)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1

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

    @classmethod
    def bigger_or_equal(self, rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1 >= rect_2:
            return rect_1
        else:
            return rect_2

    def __ge__(self, other):
        return self.area() >= other.area()

    def __eq__(self, other):
        return self.height == other.height

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        rect_print = ""
        if self.height == 0 or self.width == 0:
            return rect_print

        for i in range(self.height):
            for j in range(self.width):
                rect_print += str(self.print_symbol)
            if i != self.height - 1:
                rect_print += "\n"
        return rect_print

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)
