#!/usr/bin/python3

"""This Module defines a function that simply says the name
it was given
"""


def say_my_name(first_name, last_name=""):
    """This function prints the given name
    Args:
        first_name(string): The first name
        last_name(string): The last name, optional

    Returns:
        Returns nothing
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
