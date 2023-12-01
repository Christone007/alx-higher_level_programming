#!/usr/bin/python3


def element_at(my_list, idx):
    """Returns an element at specified index"""

    if my_list == None or len(my_list) == 0:
        return None
    elif idx < 0:
        return None
    elif idx > len(my_list) - 1:
        return None
    return my_list[idx]

