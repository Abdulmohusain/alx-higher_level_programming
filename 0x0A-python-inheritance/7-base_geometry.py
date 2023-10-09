#!/usr/bin/python3
"""this module contains BaseGeometry class"""


class BaseGeometry:
    """defines BaseGeometry class"""

    def area(self):
        """Computes the area of the geometry"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value validator"""

        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
