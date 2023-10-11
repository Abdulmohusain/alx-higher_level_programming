#!/usr/bin/python3
"""this module contains from_json_string function"""
import json


def class_to_json(obj):
    """function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object:
    Args:
        obj (object): is an instance of a Class
    """
    name, number = str(obj).replace("[MyClass] ", '').replace("-", "").split()

    new_dict = {}
    new_dict["name"] = name
    new_dict["number"] = number
    return json.dumps(new_dict)
