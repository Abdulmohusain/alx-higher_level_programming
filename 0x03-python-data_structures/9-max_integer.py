#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    if type(my_list) is list:
        big = my_list[0]
        for i in my_list[1:]:
            if i > big:
                big = i
        return big
