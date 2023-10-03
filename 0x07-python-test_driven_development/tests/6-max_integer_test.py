#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for function max_integer that retuns
    the maximum value in a list"""


    def test_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([5, 1, 2, 3, 4]), 5)
        self.assertEqual(max_integer([5, 1, 9, 2, 3, 4]), 9)
        self.assertEqual(max_integer([5, -1, 9, 2, -3, 4]), 9)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([3.5, 6, 8.5]), 8.5)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer(["23"]), '23')
        self.assertEqual(max_integer(["23", "ghu"]), 'ghu')
        
    def test_exception(self):
        self.assertRaises(TypeError, max_integer, 23)
        self.assertRaises(TypeError, max_integer, ["23", 6, "ghu"])
        self.assertRaises(TypeError, max_integer, [5, -1, 9, 2, -3, "fg"])
        self.assertRaises(TypeError, max_integer, [5, -1, 9, 2, -3, []])
                                                