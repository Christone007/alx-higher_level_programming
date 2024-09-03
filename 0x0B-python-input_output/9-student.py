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

    def to_json(self):
        """Returns a json serializable object representation"""

        return self.__dict__
