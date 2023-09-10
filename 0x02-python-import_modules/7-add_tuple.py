#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if type(tuple_a) is tuple and type(tuple_b) is tuple:
        if len(a) < 1 or len(b) < 1:

        
        if len(a) < 2 or len(b) < 2:
            return a[0], b[0]
        if len(a) < 2:
            return (a[0] + b[0]), b[0]
        if len(b) < 2:
            return b[0], (a[0] + b[0])
        elif len(a) >+ 2:



tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

