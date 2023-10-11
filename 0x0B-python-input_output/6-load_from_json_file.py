#!/usr/bin/python3
"""this module contains from_json_string function"""
import json


def load_from_json_file(filename):
    """a function that creates an Object to a text
    file, using a JSON representation:
    Args:
        filename (str): the file name
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
