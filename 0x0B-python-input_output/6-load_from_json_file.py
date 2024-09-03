#!/usr/bin/python3

"""This Module deserializes an object from a file"""

import json


def load_from_json_file(filename):
    """Loads and deserializes a json file"""

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
