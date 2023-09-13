#!/usr/bin/python3
"""Unique add"""


def uniq_add(my_list=[]):
    """Unique add"""

    if type(my_list) is not list:
        return
    summ = 0
    found_elements = []
    for i in my_list:
        if i in found_elements:
            continue
        summ += i
        found_elements.append(i)
    return summ
