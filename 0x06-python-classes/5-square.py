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

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private attribute __size to value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retrive the area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print("")
            return
        [print("#" * self.__size) for i in range(self.__size)]
