#!/usr/bin/python3

"""This module appends to a file"""


def append_write(filename="", text=""):
    """Appends a text to a file

    Args:
        filename(str): The name of the file
        text(str): The string to be appended

    Returns:
        The number of characters added
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
