#!/usr/bin/python3


def no_c(my_string):
    """remove all 'c's from a string"""

    if my_string is None:
        return None

    new_string = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        new_string += char
    return new_string
