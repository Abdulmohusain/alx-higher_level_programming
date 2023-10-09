#!/usr/bin/python3
"""This module contains lookup function"""


def lookup(obj):
    """ function that returns the list of available
    attributes and methods of an object
    Args:
        obj (any type): any bpython object
    """
    return dir(obj)
