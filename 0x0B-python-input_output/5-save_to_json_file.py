#!/usr/bin/python3

"""This module serializes an object and saves to a file"""

import json


def save_to_json_file(my_obj, filename):
    """Serialize an object and save to a file"""

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
