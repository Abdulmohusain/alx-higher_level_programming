#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if type(a_dictionary) is not dict:
        return
    dict_to_del = []
    for dict_key, dict_value in a_dictionary.items():
        if dict_value == value:
            dict_to_del.append(dict_key)
    for i in dict_to_del:
        del a_dictionary[i]
    return a_dictionary
