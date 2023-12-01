#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in list"""

    if my_list == []:
        return []
    return [x % 2 == 0 for x in my_list]
