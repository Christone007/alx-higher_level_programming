#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """Updates values in a dictionary"""

    if a_dictionary is None:
        return None
    elif key is None or value is None:
        return a_dictionary
    else:
        a_dictionary[key] = value
        return a_dictionary
