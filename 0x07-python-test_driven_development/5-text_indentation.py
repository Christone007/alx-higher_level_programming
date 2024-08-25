#!/usr/bin/python3

"""This module defines a function that formats text
"""


def text_indentation(text):
    """This function processes the text by adding 2
    blank lines after every '.', '?' and ':'
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print("{}".format(text[i]), end="")

        if text[i] in (".", "?", ":"):
            print("\n")
            while text[i + 1] == " ":
                i += 1
        i += 1
