#!/usr/bin/python3
"""this module contains is_same_class function"""


def is_same_class(obj, a_class):
    """ function that returns True if the object is exactly an
    instance of the specified class ; otherwise False.
    Args:
        obj: The object
        a_class: the class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
