#!/usr/bin/python3
"""This module defines a function that prints a name"""


def say_my_name(first_name="", last_name=""):
    """This function simply prints a fullname

    ::
        >>> say_my_name("Emeka", "Nwaburu")
        My name is Emeka Nwaburu
    """
    first_name = first_name
    last_name = last_name

    if not isinstance(first_name, str) or first_name == "":
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
