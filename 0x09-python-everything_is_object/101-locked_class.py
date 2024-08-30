#!/usr/bin/python3

"""Creates a Locked Class"""


class LockedClass():
"""Creates a locked class that does not permit creation of new attributes other than the first_name attribute"""

    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)

        return getattr(self, name)
