#!/usr/bin/python3

"""Redefine lists"""


class MyList(list):
    """A class derived from the default list class"""

    def print_sorted(self):
        """Prints a sorted list"""

        return self.sort()
