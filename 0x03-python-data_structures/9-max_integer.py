#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    i = 0
    j = i + 1

    while j < length:
        if my_list[i] > my_list[j]:
            tmp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = tmp
        j += 1
        i += 1
    return my_list[length - 1]
