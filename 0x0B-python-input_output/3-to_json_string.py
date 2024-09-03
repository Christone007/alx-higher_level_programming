#!/usr/bin/python3

"""This Module is used to Serialize a string"""

import json


def to_json_string(my_obj):
    """Serializes an object"""

    return json.dumps(my_obj)
