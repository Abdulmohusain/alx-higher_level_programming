#!/usr/bin/python3
"""Test 1. Test for base class in base.py"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestBaseClass1(unittest.TestCase):
    """Test for Base class"""

    def test_base_1(self):
        """Base"""
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

    def text_bas_16(self):
        """test for save_to_file function"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            data = file.read()
        self.assertEqual(data, "[]")

        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:
            data = file.read()
        self.assertEqual(data, "[]")

        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            data = file.read()
        a = [
            {"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},
            {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}
            ]
        self.assertEqual(data, a)

    def test_base_17(self):
        """test for from_json_string"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string(""), [])
        self.assertEqual(Rectangle.from_json_string(json_list_input),
                         list_input)


if __name__ == "__main__":
    unittest.main()
