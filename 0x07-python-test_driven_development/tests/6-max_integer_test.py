"""Test file for function max_integer; which find
    and return the max integer in a list of integers
    If the list is empty, the function returns None
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function"""

    def test_float(self):
        """Test normal cases float and no argument case"""
        self.assertEqual(max_integer([0, 1, -3, 7.3, 29, -5.8885]), 29)
        self.assertEqual(max_integer([29, 0, 1, -3, 7.3, -5.8885]), 29)
        self.assertEqual(max_integer([0, 1, -3, 7.3, -5.8885, 29]), 29)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_type(self):
        """tests for type error"""
        self.assertRaises(TypeError, max_integer, 21)
        self.assertRaises(TypeError, max_integer, [0, 1, -3, 7, 29, "r"])

    def test_integers(self):
        """Test for positive and negtive integer"""
        self.assertEqual(max_integer([1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -1, -1, -1, -1]), -1)
        self.assertEqual(max_integer([0, 1, 3, 7, 29, 5]), 29)
        self.assertEqual(max_integer([0, -1, -3, -7, -29, -5]), 0)
        self.assertEqual(max_integer([0, -1, 3, -7, 29, -5]), 29)


if __name__ == "__main__":
    unittest.main()
