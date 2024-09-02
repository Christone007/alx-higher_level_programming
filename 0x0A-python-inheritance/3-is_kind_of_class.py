#!/usr/bin/python3

"""This module checks if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Checks if an object belongs to a class

    Args:
        obj: An object
        a_class: A class

    Returns:
        True if obj is an instance of class, else returns false
    """

    return isinstance(obj, a_class)
