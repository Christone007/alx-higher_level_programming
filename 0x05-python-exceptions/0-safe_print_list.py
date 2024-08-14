#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    try:
        printed = 0
        i = 0

        while i < x:
            print("{}".format(my_list[i]), end="")
            i = i + 1
            printed = printed + 1
    except IndexError as e:
        pass

    finally:
        print()
        return printed
