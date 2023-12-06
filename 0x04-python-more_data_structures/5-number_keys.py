#!/usr/bin/python3


def number_keys(a_dictionary):
    """Count the dictionary keys"""

    if a_dictionary is None:
        return None
    elif type(a_dictionary) is not dict:
        return None

    return len(list(a_dictionary))
