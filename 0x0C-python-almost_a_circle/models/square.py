#!/usr/bin/python3

"""This is a Square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Gets the square size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of square objects"""
        try:
            self.width = value
            self.height = value
        except Exception:
            raise

    def update(self, *args, **kwargs):
        """Updates the square object"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            try:
                for k, v in kwargs.items():
                    setattr(self, k, v)
            except Exception:
                pass
