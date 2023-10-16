#!/usr/bin/python3
"""Test 1. Test for base class in base.py"""
import unittest
from models.base import Base


class TestBaseClass1(unittest.TestCase):
    """Test for Base class"""

    def test_base_1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

        b6 = Base(-32)
        self.assertEqual(b6.id, -32)

        b7 = Base(0)
        self.assertEqual(b7.id, 0)


