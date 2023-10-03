"""This module contains a function
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.

    Args:
        matrix (list): list of lists
        div (int or float): divisor
    """

    # checks for type and zero division error
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of "
                        "lists) of integers/floats")
    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of "
                        "lists) of integers/floats")
    row_len = len(matrix[0])
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of "
                            "lists) of integers/floats")
        if len(i) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        # loop through matrix to check if it contains int/floats
        # if not raise type error
        for item in i:
            if type(item) is not int and type(item) is not float:
                raise TypeError("matrix must be a matrix (list of "
                                "lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # divide matrix by div
    outer = []
    for lis in matrix:
        inner = []
        for item in lis:
            inner.append(round(item / div, 2))
        outer.append(inner)
    return outer
