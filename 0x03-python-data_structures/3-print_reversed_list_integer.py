#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Print a list in reverse"""

    if my_list == []:
        print(my_list)
    else:
        my_list.reverse()

        for i in my_list:
            print("{}".format(int(i)))
