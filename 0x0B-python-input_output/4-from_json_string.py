#!/usr/bin/python3
"""this module contains from_json_string function"""
import json


def from_json_string(my_str):
    """a function that returns a python object class
    from json
    Args:
        my_str (str): the string
    """
    return json.loads(my_str)
