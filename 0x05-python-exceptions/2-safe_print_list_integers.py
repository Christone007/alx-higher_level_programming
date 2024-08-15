#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """print only the integers"""
    printed = 0
    i = 0

    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            i = i + 1
            pass
        else:
            i = i + 1
            printed = printed + 1

    print()
    return printed
