#!/usr/bin/python3
"""this module contains inherits_from function"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class ; otherwise False.
    Args:
        obj: the object
        a_class: the class

    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)

    

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))