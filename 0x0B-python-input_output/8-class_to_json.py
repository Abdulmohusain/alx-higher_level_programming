#!/usr/bin/python3
"""this module contains from_json_string function"""


def class_to_json(obj):
    """function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object:
    Args:
        obj (object): is an instance of a Class
    """
    return obj.__dict__
