#!/usr/bin/python3

"""
This Module contains code that searches for text and inserts
new text
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a new line of text to a file, after each line containing
    a specific string
    """

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    newlines = []

    for line in lines:
        newlines.append(line)

        if search_string in line:
            newlines.append(new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(newlines)
