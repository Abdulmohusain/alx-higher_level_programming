#!/usr/bin/python3
"""this module contains Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this defines Square class that inherits from BaseGeometry"""
    def __init__(self, size):
        """The initialization method"""

        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Return a nice printable format of object"""
        return "[{}] {}/{}".format("Rectangle", self.__size, self.__size)

    def area(self):
        """computes the area"""
        return self.__size * self.__size
