#!/usr/bin/python3

"""This module writes text to a file and creates the file
if it doesn't exist already
"""


def write_file(filename="", text=""):
    """Writes to a file
    Args:
        filename(str): The name of the file
        text(str): The text to write to the file

    Returns:
        The number of characters written to the file
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
