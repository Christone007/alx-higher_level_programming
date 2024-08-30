#!/usr/bin/python3

"""Creates a Locked Class"""


class LockedClass():

    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)

        return getattr(self, name)
