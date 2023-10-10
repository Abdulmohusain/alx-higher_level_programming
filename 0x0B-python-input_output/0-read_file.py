#!/usr/bin/python3
"""This module contains read_file() function that reads a file"""


def read_file(filename=""):
    """Function that reads a file
    Args:
        filename (str): the filename
    """
    with open(file=filename, encoding="utf-8") as file:
        string = file.read()
        print(string, end="")
