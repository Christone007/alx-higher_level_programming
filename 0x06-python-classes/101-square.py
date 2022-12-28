#!/usr/bin/python3
"""This is a Module to demonstrate the creation
of classes in python
"""


class Square:
    """This is a class for Square shape objects.

    Attributes:
        size (int): The length of the square
        position (int, int): The cordinates

    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for y in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        my_str = ""
        if self.__size == 0:
            return "\n"
        else:
            for y in range(self.__position[1]):
                my_str += "\n"
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    my_str += " "
                for j in range(self.__size):
                    my_str += "#"
                if i is not self.__size - 1:
                    my_str += "\n"
        return my_str
