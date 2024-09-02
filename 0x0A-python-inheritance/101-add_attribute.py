#!/usr/bin/python3

"""A Module for adding attributes to objects if possible"""


def add_attribute(obj, name, value):
    """Adds an attribute to an object if the object is mutable"""

    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    
    obj.name = value
