#!/usr/bin/python3
"""This module defines a function that helps
to parse text"""


def text_indentation(text=""):
    """Function that parses text to create
    new lines seperated by a newline after 
    every `:`, `?`, and `.` character"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):
        if text[i] != " ":
            break
        else:
            i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.','?',':']:
            print("\n")
            while text[i + 1] == " ":
                i += 1
        i += 1
