#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """Retrieve differences"""

    if set_1 is None or set_2 is None:
        return {}

    return set_1 ^ set_2
