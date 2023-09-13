#!/usr/bin/python3
"""function that deletes a key in a dictionary."""

def multiply_list_map(my_list=[], number=0):
    """returns a list with all values multiplied
    by a number"""
    if type(my_list) is not list:
        return
    if len(my_list) == 0:
        return
    return [i * 2 for i in my_list[:]]
