#!/usr/bin/python3
"""Unittest for max_integer() function in the
`6-max_integer.py` module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([6, 4, 2, 10]), 10)
        self.assertAlmostEqual(max_integer([-2, 4, -10, 5]), 5)
        self.assertAlmostEqual(max_integer([6]), 6)

    def test_empty(self):
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(), None)

    def test_string(self):
        self.assertAlmostEqual(max_integer("aecdb"), "e")
