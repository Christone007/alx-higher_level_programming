#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """Delete an element from a dictionary"""

    if a_dictionary is None:
        return None
    elif type(a_dictionary) is not dict:
        return None
    elif key == "":
        return a_dictionary

    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
