#!/usr/bin/python3
"""This module contains write_file() function that writes a file"""


def write_file(filename="", text=""):
    """Function that writes a file
    Args:
        filename (str): the filename
    """
    with open(file=filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
