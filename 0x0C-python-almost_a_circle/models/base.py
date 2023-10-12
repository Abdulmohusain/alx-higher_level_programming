#!/usr/bin/python3
"""Base class"""


class Base:
    """This defines the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
