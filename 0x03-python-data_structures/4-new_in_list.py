#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Make a copy and replace an element"""

    if my_list is None:
        return None
    elif idx < 0 or idx is None or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        temp_list = my_list.copy()
        temp_list[idx] = element
        return temp_list
