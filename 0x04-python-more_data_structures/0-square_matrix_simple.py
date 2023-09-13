#!/usr/bin/python3
"""Square matrix calculation"""


def square_matrix_simple(matrix=[]):
    """calculate the square of matrix"""

    if type(matrix) is not list:
        return
    b = []
    for i in matrix:
        a = []
        for j in i:
            a.append(j ** 2)
        b.append(a)
    return b
