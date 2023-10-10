#!/usr/bin/python3
"""this module contains rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this defines Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """The initialization method"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return a nice printable format of object"""
        return "[{}] {}/{}".format(type(self.__class__), self.__width, self.__height)

    def area(self):
        """computes the area"""
        return self.__width * self.__height

r = Rectangle(3, 5)

print(r)
print(r.area())
