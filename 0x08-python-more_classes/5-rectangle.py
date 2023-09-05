#!/usr/bin/python3
"""Module for class Rectangle"""


class Rectangle:
    """Creates a rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes the class"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    def __str__(self):
        """returns “informal” or nicely printable string
        representation of an object"""
        if self.__height == 0 or self.__width == 0:
            return ""
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """returns “official” string representation of an object."""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Detect Instance deletion"""
        print("Bye rectangle...")

    @property
    def width(self):
        """Return private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
