#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if type(my_list) is list:
        my_list.reverse()
        for m in my_list:
            print("{:d}".format(m))
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
