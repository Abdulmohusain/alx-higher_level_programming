#!/usr/bin/python3
"""this module contains from_json_string function"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text
    file, using a JSON representation:
    Args:
        my_obj (str): the string
        filename (str): the file name
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
