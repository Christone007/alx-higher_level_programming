#!/usr/bin/python3
"""Unittest for the square.py module"""

import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """A unittest class for the Square class"""

    """
    def test_01_setId(self):
        #Tests if IDs are correctly set
        s1 = Square(4)
        self.assertEqual(s1.id, 1)

        s2 = Square(4, 0, 0, 5)
        self.assertEqual(s2.id, 5)"""

    def test_02_attributes(self):
        """Test if other attributes are correctly set"""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

        s2 = Square(5, 1, 3)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 3)

    def test_03_area(self):
        """Tests if area is well calculated"""
        s3 = Square(5, 1, 3, 10)
        self.assertEqual(s3.area(), 25)

    def test_04_setter(self):
        """Tests if the size setter works well"""
        s1 = Square(5, 1, 3)
        s1.size = 2
        self.assertEqual(s1.size, 2)
    
    def test_05_update(self):
        """See that args and kwargs work well in update"""
        s1 = Square(5, 1, 2, 4)
        s1.update(6)
        self.assertEqual(s1.id, 6)
        s1.update(6, 3)
        self.assertEqual(s1.size, 3)
        s1.update(6, 3, 0)
        self.assertEqual(s1.x, 0)
        s1.update(6, 3, 0, 10)
        self.assertEqual(s1.y, 10)
        s1.update(12, id=5)
        self.assertEqual(s1.id, 12)
        s1.update(size=12, id=5, x=5, s=7)
        self.assertNotEqual(s1.y, 7)
        self.assertEqual(s1.y, 10)

    def test_06_to_dictionary(self):
        """Checks square to dictionary Conversion"""
        s1 = Square(5, 1, 2, 4)
        self.assertEqual(s1.to_dictionary(),
                {"id":4,"size":5,"x":1, "y":2})
