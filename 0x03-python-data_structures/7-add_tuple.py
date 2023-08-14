#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return
    if type(tuple_a) is tuple and type(tuple_b) is tuple:
            if len(tuple_a) >= 2:
                a, b = tuple_a
            elif len(tuple_a) == 1:
                a = tuple_a[0]
                b = 0
            else:
                a2 = 0
                b2 = 0
            if len(tuple_b) >= 2:
                a2, b2 = tuple_b
            elif len(tuple_b) == 1:
                a2 = tuple_b[0]
                b2 = 0
            else:
                a2 = 0
                b2 = 0
            return a + a2, b + b2
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
