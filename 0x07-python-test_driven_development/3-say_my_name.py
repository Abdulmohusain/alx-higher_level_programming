#!/usr/bin/python3
"""Module to divide matrix by 3
Args:
    first_name: string
    last_name: string
"""


def say_my_name(first_name, last_name=""):
    """First name and last name"""
    if type(first_name) is not str or first_name is None:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str or last_name is None:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
