#!/usr/bin/python3
"""Adds two integer
args:
    a (int): num1
    b (int): num2
"""


def add_integer(a, b=98):
    """A functions that adds two ints
    Argument: a is int b is also int
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
