#!/usr/bin/python3
"""Module for class Rectangle"""


class Rectangle:
    """Creates a rectangle class
    Args:
            width (int): width
            height (int): height
    """

    def __init__(self, width=0, height=0):
        """Instance attributes"""

        # Validate width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        # validate height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        # set width and height
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """mutates/set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """mutates/set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """"returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
