#!/usr/bin/python3
"""this module contains Square class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """this defines Square class that inherits from BaseGeometry"""
    def __init__(self, size):
        """The initialization method"""

        self.integer_validator("size", size)
        self.__size = size
    
    def area(self):
        """computes the area"""
        return self.__width * self.__height