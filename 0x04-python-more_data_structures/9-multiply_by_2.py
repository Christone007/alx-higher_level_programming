#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """Multiply all values by 2"""

    if a_dictionary is None:
        return None
    elif type(a_dictionary) is not dict:
        return None
    return {x:y * 2 for x,y in a_dictionary.items()}
