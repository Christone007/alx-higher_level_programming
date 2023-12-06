#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """Deletes keys with specific values"""

    new_dictionary = a_dictionary.copy()

    for k, v in new_dictionary.items():
        if v == value:
            del a_dictionary[k]
    return a_dictionary
