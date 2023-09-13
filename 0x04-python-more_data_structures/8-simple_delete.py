#!/usr/bin/python3
"""function that deletes a key in a dictionary."""


def simple_delete(a_dictionary, key=""):
    """function that deletes a key in a dictionary."""
    if type(a_dictionary) is not dict:
        return
    if key != "" and key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
