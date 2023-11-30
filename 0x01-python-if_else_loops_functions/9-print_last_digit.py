#!/usr/bin/python3


def print_last_digit(number):
    """Print and return the last digit of a number"""

    if number == 0:
        last_digit = 0
    elif number < 0:
        num_pos = number * (-1)
        last_digit = num_pos % 10
    else:
        last_digit = number % 10

    print("{}".format(last_digit), end="")
    return last_digit
