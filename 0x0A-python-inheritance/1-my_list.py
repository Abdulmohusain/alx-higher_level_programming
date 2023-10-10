#!/usr/bin/python3
"""This module contains class my_list with
    method to sort the list
"""


class MyList(list):
    """This defines n new list class that inherits from
        list
    """
    def print_sorted(self):
        """Function that prints sorted list"""
        for i in self:
            if type(i) is not int:
                raise TypeError("list must contain only integers")
        print(sorted(self))
