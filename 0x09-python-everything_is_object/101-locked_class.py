#!/usr/bin/python3

"""This module defines a locked class
"""


class LockedClass:
    """Restricts objects from creating extra attributes
    """
    __slot__ = ["first_name"]

    def __init__(self):
        pass
