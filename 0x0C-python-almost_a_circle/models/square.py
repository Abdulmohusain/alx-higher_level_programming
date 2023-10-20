#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This defines a class Square
    Args:
        Rectangle (Rectangle): Class rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """"init method"""
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """ that assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
        if args:
            for n, arg in enumerate(args):
                if n == 0:
                    self.id = arg
                elif n == 1:
                    self.size = arg
                elif n == 2:
                    self.x = arg
                elif n == 3:
                    self.y = arg

    @property
    def size(self):
        """height getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.integer_validator("size", value)
        self.width = value
        self.height = value

    def __str__(self):
        """nicely printable format of Rectangle"""
        return "[Square] ({}) {}/{} - {}".format(
                                                self.id,
                                                self.x,
                                                self.y,
                                                self.width,
                                                )
