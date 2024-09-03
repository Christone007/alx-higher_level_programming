#!/usr/bin/python3

"""This Module adds arguments to a list and then serializes it"""

import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main(args):
    filename = "add_item.json"

    try:
        obj_list = load_from_json_file(filename)
    except FileNotFoundError:
        obj_list = []

    obj_list += args
    save_to_json_file(obj_list, filename)


if __name__ == "__main__":
    main(sys.argv[1:])
