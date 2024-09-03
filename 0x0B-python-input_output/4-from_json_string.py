#!/usr/bin/python3

"""This module deserializes a JSON string"""

import json


def from_json_string(my_str):
    """Deserializes a json string"""

    return json.loads(my_str)
