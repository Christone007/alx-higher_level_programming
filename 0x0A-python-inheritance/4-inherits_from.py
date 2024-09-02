#!/usr/bin/python3

"""Checks if its an object of a child class"""


def inherits_from(obj, a_class):
    """Checks if an object belongs to a child class

    Args:
        obj: An object
        a_class: a class

    Returns:
        True: if 'obj' belongs to a child of 'a_class', otherwise False
    """

    return (isinstance(obj, a_class) and type(obj) is not a_class)
