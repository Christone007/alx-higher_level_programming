#!/usr/bin/python3
"""This is a class that accepts only one attribute"""


class LockedClass:
    """The __slots__ attribute is defined to prevent
    the creation of a __dict__ attribute. 

    Hence, the user of this program can only create
    objects with only one attribute `first_name`
    """
    __slots__ = 'first_name'
