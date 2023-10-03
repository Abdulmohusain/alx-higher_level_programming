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

    def __str__(self):
        """ return a nicely printable reprrsentation of the object"""
        nice_string = ""
        if self.__height == 0 or self.__width == 0:
            return nice_string
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    nice_string += "#"
                if i < self.__height - 1:
                    nice_string += "\n"
        return nice_string

    def __repr__(self):
        """return a string representation of the
         rectangle to be able to recreate a new
        instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """return private instance attribute width"""
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
        """return private instance attribute height"""
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
        """"returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
