#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Print a list in reverse"""

    if my_list == []:
        print (my_list)
    else:
        temp_list = my_list.copy()
        temp_list.reverse()

        for i in temp_list:
            print("{:d}".format(i))
