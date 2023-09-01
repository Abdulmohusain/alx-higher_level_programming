#!/usr/bin/python3
"""This module creates a Square class"""


class Square:
    """This create the class square"""

    def __init__(self, size=0):
        """All attributes are instantiated

        Args:
            size (int): Length of square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area"""
        return self.__size ** 2
