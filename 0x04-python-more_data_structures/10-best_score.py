#!/usr/bin/python3
"""function that deletes a key in a dictionary."""


def best_score(a_dictionary):
    """returns a key with the biggest integer value"""

    if type(a_dictionary) is not dict:
        return
    new = a_dictionary.copy()
    for key, value in new.items():
        largest = value
        largest_key = key
        break
    for key, value in new.items():
        if value > largest:
            largest_key = key
    return largest_key
