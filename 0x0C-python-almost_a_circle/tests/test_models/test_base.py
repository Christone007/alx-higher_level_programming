#!/usr/bin/python3
""" This is a unittest file for the
models/base.py module"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests the Base class"""
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(4)
        self.assertEqual(b3.id, 4)
        b4 = Base()
        self.assertEqual(b4.id, 3)
