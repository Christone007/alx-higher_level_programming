#!/usr/bin/python3

"""Checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Checks if an object belongs to a class"""

    return (type(obj) is a_class)
