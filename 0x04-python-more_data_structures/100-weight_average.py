#!/usr/bin/python3


def weight_average(my_list=[]):
    """returns a weighted average"""

    if my_list == []:
        return 0

    product = 0
    count = 0

    for elem in my_list:
        if type(elem) is not tuple or len(elem) != 2:
            return 0
        product += (elem[0] * elem[1])
        count += elem[1]

    return product / count
