#!/usr/bin/python3

"""The add integer module"""


def add_integer(a, b=98):
    """Adds two integers and returns an integer"""
    if not (
            isinstance(a, int) or
            isinstance(a, float)
            ):
        raise TypeError("a must be an integer")
    if not (
            isinstance(b, int) or
            isinstance(b, float)
            ):
        raise TypeError("b must be an integer")
    if a is None or b is None:
        raise ValueError

    return int(a) + int(b)
