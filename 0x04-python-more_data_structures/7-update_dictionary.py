#!/usr/bin/python3
"""Update dict """


def update_dictionary(a_dictionary, key, value):
    """ update dict"""

    if type(a_dictionary) is not dict\
            or type(key) is not str:
        return
    a_dictionary[key] = value
    return a_dictionary
