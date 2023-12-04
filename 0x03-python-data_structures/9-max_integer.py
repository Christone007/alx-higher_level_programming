#!/usr/bin/python3


def max_integer(my_list=[]):
    """Returns the maximum integer"""

    if type(my_list) == list:
        if my_list == []:
            return None
        else:
            max = 0
            for i in my_list:
                if i > max:
                    max = i
            return max
