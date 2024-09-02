#!/usr/bin/python3

"""Declares a MyInt class"""


class MyInt(int):
    """Creates a class of rebel integers"""

    def __init__(self, value):
        """Initializes an integer"""

        self.__value = value

    def __eq__(self, other):
        """A rebel case that returns True for unequal items"""

        return self.__value != other

    def __ne__(self, other):
        """A rebel case that returns True for equal items"""

        return self.__value == other
