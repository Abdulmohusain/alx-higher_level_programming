#!/usr/bin/python3
"""Sorted dict"""


def print_sorted_dictionary(a_dictionary):
    """Print sorted dict"""
    if type(a_dictionary) is not dict:
        return
    for key, value in sorted(a_dictionary.items()):
        print("{:s}: {}".format(key, value))
