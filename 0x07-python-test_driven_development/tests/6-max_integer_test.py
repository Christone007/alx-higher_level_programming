#!/usr/bin/python3
"""Unittest for max_integer() function in the
`6-max_integer.py` module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([6, 4, 10, 1]), 10)
    
    def test_max_at_end(self):
        self.assertAlmostEqual(max_integer([-2, 4, -10, 5]), 5)
        self.assertAlmostEqual(max_integer([-15, -8,- 11, -7]), -7)

    def test_max_at_start(self):
        self.assertAlmostEqual(max_integer([6, 2, 5]), 6)
        self.assertAlmostEqual(max_integer([-5, -12, -20]), -5)

    def test_max_in_middle(self):
        self.assertAlmostEqual(max_integer([6, 7, 2]), 7)
        self.assertAlmostEqual(max_integer([-2, 0, -1]), 0)

    def test_single_element(self):
        self.assertAlmostEqual(max_integer([6]), 6)
        self.assertAlmostEqual(max_integer([-7]), -7)

    def test_empty(self):
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(), None)

    def test_string(self):
        self.assertAlmostEqual(max_integer("aecdb"), "e")

    def test_float(self):
        self.assertAlmostEqual(max_integer([2.3, 1.0, 5.7]), 5.7)
