#!/usr/bin/python3

"""This Module defines a class that has a method to
generate a serializable object representation
"""


class Student:
    """A Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a json serializable object representation"""
        my_dict = {}
        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is str and attr in self.__dict__:
                    my_dict[attr] = self.__dict__[attr]
        else:
            my_dict = self.__dict__

        return my_dict

    def reload_from_json(self, json):
        """Loads an object's attributes from a json serializable dict"""
        self.__dict__ = {}
        for k, v in json.items():
            self.__dict__[k] = v
