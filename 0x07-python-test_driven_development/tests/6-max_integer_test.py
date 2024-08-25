#!/usr/bin/python3

"""This is a unittest module"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """This is a module containing unittests for the 
    function max_integer
    """

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_at_end(self):
        self.assertEqual(max_integer([2, 3]), 3)

    def test_all_equal(self):
        self.assertEqual(max_integer([4, 4, 4]), 4)
        self.assertEqual(max_integer([6]), 6)

    def test_negatives_and_positives(self):
        self.assertEqual(max_integer([-2, 0, 5, -10]), 5)
       
    def test_zeros(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_all_negatives(self):
        self.assertEqual(max_integer([-20, -4, -5, -10]), -4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 3, 9, -2]), 10)
