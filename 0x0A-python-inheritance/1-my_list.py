#!/usr/bin/python3

"""Redefine lists"""


class MyList(list):
    """A class derived from the default list class"""
    def __init__(self):
        """initializes the object"""

        super().__init__()

    def print_sorted(self):
        """Prints a sorted list"""

        print(sorted(self))
