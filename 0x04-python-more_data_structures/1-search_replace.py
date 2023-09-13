#!/usr/bin/python3
"""Search replace """


def search_replace(my_list, search, replace):
    """Search replace"""

    if type(my_list) is not list:
        return
    list_copy = my_list[:]
    for i, j in enumerate(list_copy):
        if j == search:
            list_copy.remove(j)
            list_copy.insert(i, replace)
    return list_copy
