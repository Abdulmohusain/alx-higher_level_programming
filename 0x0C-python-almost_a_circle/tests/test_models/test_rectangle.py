#!/usr/bin/python3
"""Test 1. Test for rectangle class in rectangle.py"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestReactangle2(unittest.TestCase):
    """Tests cases for Reactangle class"""

    def test_rectangle_2(self):
        """Test for 2-rectangle"""
        # check inheritance
        r1 = Rectangle(2, 3)
        self.assertTrue(issubclass(type(r1), Base))
        with self.assertRaises(TypeError):
            r1 = Rectangle()
            r2 = Rectangle(1)

        # Test for instanca attributes and their getter
        # Test for setters is found below
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        # self.assertEqual(r1.id, 3)

        r2 = Rectangle(2, 4, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(2, 4, 2, 3)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r3.x, 2)
        self.assertEqual(r3.y, 3)
        # Test for setters
        r4 = Rectangle(2, 4, 2, 3, 100)
        self.assertEqual(r4.width, 2)
        r4.width = 3
        self.assertEqual(r4.width, 3)

        self.assertEqual(r4.height, 4)
        r4.height = 2
        self.assertEqual(r4.height, 2)

        self.assertEqual(r4.x, 2)
        r4.x = 4
        self.assertEqual(r4.x, 4)

        self.assertEqual(r4.y, 3)
        r4.y = 4
        self.assertEqual(r4.y, 4)


class TestReactangle3(unittest.TestCase):
    """Tests cases for Reactangle class"""
    def test_rectangle_3(self):
        """Test for 3-rectangle"""
        # Test for type error

        with self.assertRaises(TypeError):
            Rectangle("a", 2, 4, 6, 8)
            Rectangle(1, 7.43, 4, 6, 8)
            Rectangle(1, 2, [], 6, 8)
            Rectangle(1, 2, 4, True, 8)
            Rectangle(1, 2, 4, 6, 3+5j)

        # Test for Value error
        # Width
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 4, 6, 8)
            Rectangle(-2, 2, 4, 6, 8)

        # Height
        with self.assertRaises(ValueError):
            Rectangle(1, 0, 4, 6, 8)
            Rectangle(1, -2, 4, 6, 8)

        # x
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3, 6, 8)

        # y
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -8, 6, 8)

        # id
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 4, 6, -2)
            Rectangle(1, 2, 4, 6, 0)

        # Setter validiation following the order above
        r4 = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaises(TypeError):
            r4.width = []
            r4.height = ""
            r4.x = 4.65
            r4.y = {}
        with self.assertRaises(ValueError):
            r4.width = 0
            r4.width = -1
            r4.height = 0
            r4.height = -1
            r4.x = 0
            r4.x = -1
            r4.y = 0
            r4.y = -1


class TestReactangle4(unittest.TestCase):
    """Tests cases for Reactangle class"""
    def test_rectangle_4(self):
        """Test for 4-rectangle"""
        r1 = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(r1.area(), 8)

    # def test_rectangle_5(self):
    #     """Test for 5-rectangle"""
    #     r1 = Rectangle(2, 4, 6, 8, 10)
    #     b = "\n\n\n\n\n\n\n\n      ##\n      ##\n      ##\n      ##\n"
    #     self.assertEqual(r1.display(), b)


class TestReactangle6(unittest.TestCase):
    """Tests cases for Reactangle class"""
    def test_rectangle_6(self):
        """Test for 6-rectangle"""
        r1 = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(str(r1), "[Rectangle] (10) 6/8 - 2/4")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (9) 1/0 - 5/5")

    # def test_rectangle_7(self):
    #     """Test for 7-rectangle"""
    #     r1 = Rectangle(2, 3, 2, 2)
    #     self.assertEqual(r1.display(), "\n\n\n  ##\n  ##\n  ##\n")


class TestReactangle8(unittest.TestCase):
    """Tests cases for Reactangle class"""
    def test_rectangle_8(self):
        """Test for 8-rectangle"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (10) 10/10 - 10/10")

        # self.assertRaises(r1.update(), TypeError)

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")


class TestReactangle9(unittest.TestCase):
    """Tests cases for Reactangle class"""
    def test_rectangle_9(self):
        """Test for 9-rectangle"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (11) 10/10 - 10/10")

        # self.assertRaises(r1.update(), TypeError)

        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (11) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (11) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")


class TestReactangle13(unittest.TestCase):
    """Tests cases for Reactangle class"""
    def test_rectangle_13(self):
        """Test for to_dictionary"""
        r1 = Rectangle(10, 7, 2, 8, 23)
        self.assertEqual(
                        str(r1.to_dictionary()),
                        "{'id': 23, 'width': 10, 'height': 7, 'x': 2, 'y': 8}"
                        )


if __name__ == "__main__":
    unittest.main()
