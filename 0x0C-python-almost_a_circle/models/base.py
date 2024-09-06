#!/usr/bin/python3

"""
This module creates a base class
"""
import json


class Base:
    """
    The Base Class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialize a dictionary or list into JSON"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        try:
            json_data = json.dumps(list_dictionaries)
        except Exception:
            pass

        return json_data
