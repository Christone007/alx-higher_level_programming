#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Print a list in reverse"""

    if my_list is not None or len(my_list) > 1:
        my_list.reverse()

        for i in my_list:
            print("{:d}".format(str(i)))
    else:
        print(my_list)
