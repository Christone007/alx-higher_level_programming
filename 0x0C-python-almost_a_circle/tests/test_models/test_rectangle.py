#!/usr/bin/python3
"""A unittest module for the rectangle.py module"""

import unittest
from models.base import Base
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class"""


    """
    def test_01_id(self):
        #Tests the assignment of IDs

        r1 = Rectangle(5, 3)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(5, 3, 1, 1)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(5, 3, 1, 1, 6)
        self.assertEqual(r3.id, 6)

        r4 = Rectangle(5, 3, 1, 2)
        self.assertEqual(r4.id, 3)"""


    def test_02_getters(self):
        """Tests the getters of private instance attributes"""
        r1 = Rectangle(3, 5)

        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 4)


    def test_03_setters(self):
        """Tests the setters of private instance attributes"""
        r1 = Rectangle(3, 5)
        r1.x = 2
        r1.y = 3
        r1.width = 5
        r1.height = 10
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 10)

    def test_04_types(self):
        """Tests that object is created only with valid types"""
        self.assertRaises(TypeError, Rectangle, "10", 20)
        self.assertRaises(TypeError, Rectangle, 10, "20")
        self.assertRaises(TypeError, Rectangle, 10, 20, "5", 5)
        self.assertRaises(TypeError, Rectangle, 10, 20, 5, "5")
        self.assertRaises(TypeError, Rectangle, 10, 20, 5, (5, 3))
        self.assertRaises(TypeError, Rectangle, 10, {'20': 5}, 5, 5)
        self.assertRaises(TypeError, Rectangle, 10, None, 5, 5)
        self.assertRaises(TypeError, Rectangle, 10, 1.6, 5, 5)

    def test_05_values(self):
        """Tests that values are all within acceptale range"""
        self.assertRaises(ValueError, Rectangle, 0, 5)
        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, -4, 5)
        self.assertRaises(ValueError, Rectangle, 9, -3)
        self.assertRaises(ValueError, Rectangle, 5, 10, -4)
        self.assertRaises(ValueError, Rectangle, 9, 5, 0, -1)
        self.assertRaises(ValueError, Rectangle, 10, 5, 0, -1)
        self.assertRaises(ValueError, Rectangle, 6, 5, -1, 0, 8)

    def test_06_area(self):
        r1 = Rectangle(3, 5)
        self.assertEqual(r1.area(), 15)

        r2 = Rectangle(5, 20, 2, 4, 1)
        self.assertEqual(r2.area(), 100)

    """
    def test_07_display(self):
        rect = Rectangle(2, 3)
        self.assertEqual(print(rect.display()), "##\n##\n#")"""

    def test_08_str(self):
        r1 = Rectangle(3, 10, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (4) 2/3 - 3/10")

    def test_09_update(self):
        r1 = Rectangle(3, 10, 2, 3, 4)

        r1.update(2, 3, 5, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (2) 3/4 - 3/5")

        r1.update(10, 8)
        self.assertEqual(str(r1), "[Rectangle] (10) 3/4 - 8/5")

        r1.update(height=60)
        self.assertEqual(r1.height, 60)

        r1.update(id=5, width=10, height=60, x=4)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 60)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 4)

        r1.update(10, id=7)
        self.assertEqual(r1.id, 10)

    def test_10_to_dictionary(self):
        r1 = Rectangle(3, 10, 15, 2, 4)
        self.assertEqual(r1.to_dictionary(), {"height":10, "id":4, "width":3, "x":15, "y":2})

    def test_11_json(self):
        r1 = Rectangle(3, 10, 15, 2, 4)
        r1_dict = r1.to_dictionary()
        self.assertEqual(type(Base.to_json_string([r1_dict])), str)
