#!/usr/bin/python3

"""This is a unittest module"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """This is a module containing unittests for the 
    function max_integer
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2, 3]), 3)
        self.assertEqual(max_integer([-2, 0, 5, -10]), 5)
        self.assertEqual(max_integer([4, 4, 4]), 4)
        self.assertEqual(max_integer([0, 0]), 0)
        self.assertEqual(max_integer([6]), 6)
        self.assertEqual(max_integer([-20, -4, -5, -10]), -4)
