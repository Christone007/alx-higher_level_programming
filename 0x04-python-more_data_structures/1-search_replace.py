#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replace occurrence of an element by another"""

    if my_list is None or type(my_list) is not list:
        return None
    elif search is None or replace is None:
        return None
    elif len(my_list) == 0:
        return my_list

    return list(map(lambda x: replace if x == search else x, my_list))
