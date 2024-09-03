#!/usr/bin/python3

"""This Module reads a text file"""


def read_file(filename=""):
    """This function reads a file's contents

    Description:
        The assumption is that the file exists and has the required permission

    Args:
        filename(str): The name of a file

    Returns:
        Returns the content of the file
    """

    with open(filename, encoding='utf-8') as f:
        print(f.read(-1), end='')
