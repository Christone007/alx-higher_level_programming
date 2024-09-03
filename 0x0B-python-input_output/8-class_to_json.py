#!/usr/bin/python3

"""This Module is for JSON serialization of an object"""


def class_to_json(obj):
    """Create a dictionary representation of an object"""

    return obj.__dict__
