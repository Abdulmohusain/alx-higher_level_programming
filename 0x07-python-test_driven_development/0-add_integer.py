"""This module contains add_integer function"""


def add_integer(a, b=98):
    """A function that adds two integer"""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
