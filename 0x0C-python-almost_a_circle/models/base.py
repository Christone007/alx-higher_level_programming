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

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON representation of objects to file"""
        try:
            filename = cls.__name__ + ".json"
            with open(filename, "w", encoding="utf-8") as f:
                if list_objs is None:
                    f.write(cls.to_json_string([]))
                else:
                    my_list_dict = [x.to_dictionary() for x in list_objs]
                    f.write(cls.to_json_string(my_list_dict))

        except Exception:
            pass

    @staticmethod
    def from_json_string(json_string):
        """Parses a JSON string into a list of dictionaries

        Args:
            json_string (str): Represents a list of dictionaries
        """

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an object from a dictionary"""
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_obj = cls(1)

        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """Parses JSON from a file into a list of objects"""
        try:
            with open(cls.__name__+".json", "r", encoding="utf-8") as f:
                saved_json = f.read()
        except FileNotFoundError:
            return []

        list_of_dicts = cls.from_json_string(saved_json)
        return [cls.create(**x) for x in list_of_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save the Objects in a CSV file"""
       try:
           with open(cls.__name__ + ".json", 'w', encoding="utf-8") as f:
               if list_objs is None or len(list_objs) == 0:
                   f.write("[]")

        except Exception:
            raise

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from a CSV file"""
        pass
