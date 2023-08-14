#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return
    if type(tuple_a) is tuple and type(tuple_b) is tuple:
        if len(tuple_a) >= 2:
            if len(tuple_b) >= 2:
                return (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])
            if len(tuple_b) == 1:
                return tuple_a[0] + tuple_b[0], tuple_a[1]
            if len(tuple_b) == 0:
                return tuple_a[0], tuple_a[1]
        if len(tuple_a) == 1:
            if len(tuple_b) >= 2:
                return tuple_a[0] + tuple_b[0], tuple_b[1]
            if len(tuple_b) == 1:
                return tuple_a[0], tuple_b[0]
            if len(tuple_b) == 0:
                return (tuple_a[0], )
        if len(tuple_a) == 0:
            if len(tuple_b) >= 2:
                return tuple_b[0], tuple_b[1]
            if len(tuple_b) == 1:
                return (tuple_b[0], )
            if len(tuple_b) == 0:
                return
