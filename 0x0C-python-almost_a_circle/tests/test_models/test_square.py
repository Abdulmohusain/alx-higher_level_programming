#!/usr/bin/python3
"""Test 1. Test for rectangle class in rectangle.py"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare10(unittest.TestCase):
    """Tests cases for Square class"""

    def test_square_10(self):
        """test for 10-square"""
        s1 = Square(2)
        self.assertTrue(issubclass(type(s1), Rectangle))
        with self.assertRaises(TypeError):
            s1 = Square()

        with self.assertRaises(ValueError):
            s1 = Square(-2, 4)
            s1 = Square(0)

        # Test for instanca attributes and their getter
        # Test for setters is found below
        s1 = Square(2)
        self.assertEqual(str(s1), "[Square] (13) 0/0 - 2")
        self.assertEqual(s1.area(), 4)

        # self.assertStdout(str(s1.display()), "##\n##")

        # Getters and setters
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.area(), 4)
        s1.size = 3
        self.assertEqual(s1.size, 3)

        self.assertEqual(s1.x, 0)
        s1.x = 4
        self.assertEqual(s1.x, 4)

        self.assertEqual(s1.y, 0)
        s1.y = 4
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.area(), 9)

        s2 = Square(4, 2)
        self.assertEqual(str(s2), "[Square] (14) 2/0 - 4")
        self.assertEqual(s2.size, 4)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.id, 14)
        self.assertEqual(s2.area(), 16)

        s3 = Square(4, 2, 3)
        self.assertEqual(str(s3), "[Square] (15) 2/3 - 4")
        self.assertEqual(s3.size, 4)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 15)

        # Test for setters
        s4 = Square(4, 2, 3, 100)
        self.assertEqual(str(s4), "[Square] (100) 2/3 - 4")
        self.assertEqual(s4.size, 4)
        s4.size = 3
        self.assertEqual(s4.size, 3)

        self.assertEqual(s4.x, 2)
        s4.x = 4
        self.assertEqual(s4.x, 4)

        self.assertEqual(s4.y, 3)
        s4.y = 4
        self.assertEqual(s4.y, 4)
        self.assertEqual(s4.id, 100)


class TestSquare12(unittest.TestCase):
    """Tests cases for Square class"""

    def test_square_12(self):
        """test for update()"""

        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (16) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")


class TestSquare14(unittest.TestCase):
    """Tests cases for Square class"""
    def test_square_14(self):
        """Test for to_dictionary"""

        s1 = Square(10, 2, 1)
        self.assertEqual(
                        str(s1.to_dictionary()),
                        "{'id': 17, 'size': 10, 'x': 2, 'y': 1}"
                        )


if __name__ == "__main__":
    unittest.main()
