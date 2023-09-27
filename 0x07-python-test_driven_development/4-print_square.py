#!/usr/bin/python3
"""Module to divide matrix by 3
Args:
    first_name: string
    last_name: string
"""


def print_square(size):
    """print # size times"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
