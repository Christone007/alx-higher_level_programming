#!/usr/bin/python3


def multiple_returns(sentence):
    """return a tuple"""

    if sentence is None or sentence == "":
        return 0, None

    length = len(sentence)
    first_char = sentence[:1]
    return length, first_char
