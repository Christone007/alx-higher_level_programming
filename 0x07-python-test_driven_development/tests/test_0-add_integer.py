#!/usr/bin/python3

import unittest
add_integer = __import__("0-add_integer").add_integer

class TestAddInteger(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_integer(2, 5), 7)
        self.assertEqual(add_integer(100, 34), 134)
        self.assertEqual(add_integer(-4, -7), -11)
        self.assertEqual(add_integer(-5, 10), 5)
        self.assertEqual(add_integer(0, 5), 5)
        self.assertEqual(add_integer(2), 100)
        self.assertEqual(add_integer(4.5, 2.4), 6)

    def test_types(self):
        self.assertRaises(TypeError, add_integer, 2, "d")
        self.assertRaises(TypeError, add_integer, 4.0, "4j+4")
        self.assertRaises(TypeError, add_integer, (4,6), 3)
        self.assertRaises(TypeError, add_integer, 5, (9,0,4))
        self.assertRaises(TypeError, add_integer, "5", 6.3)
        self.assertRaises(TypeError, add_integer, [4, 's'], 6)
        self.assertRaises(TypeError, add_integer, True, 4.2)
        self.assertRaises(TypeError, add_integer, {5, 6}, 6.3)

    def test_values(self):
        self.assertRaises(TypeError, add_integer, None)
        self.assertRaises(TypeError, add_integer, 67, None)
