#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """Print an ordered dictionary"""

    sorted_dictionary = dict(sorted(a_dictionary.items(),
        key=lambda x:x[0], reverse=False))

    for i, v in sorted_dictionary.items():
        print("{}: {}".format(i, v))
