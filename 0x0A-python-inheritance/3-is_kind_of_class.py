#!/usr/bin/python3
"""this module contains is_same_class function"""


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    Args:
        obj: the object
        a_class: the class
    """
    return isinstance(obj, a_class)
