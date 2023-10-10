#!/usr/bin/python3
"""This module contains append_write()
function that appends a file
"""


def append_write(filename="", text=""):
    """Function that appends a file
    Args:
        filename (str): the filename
    """
    with open(file=filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
