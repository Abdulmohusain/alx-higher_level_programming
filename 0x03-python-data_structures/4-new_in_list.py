#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = list()
    if idx < 0 or idx > len(my_list) - 1:
        for i in my_list:
            new_list.append(i)
        return new_list
    if type(my_list) is list:
        for i in my_list:
            if my_list.index(i) == idx:
                new_list.append(element)
                continue
            new_list.append(i)
        return new_list
