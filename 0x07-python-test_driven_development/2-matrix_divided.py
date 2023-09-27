#!/usr/bin/python3
"""Module to divide matrix by 3
Args:
    matrix: list
    div: the divisor
"""


def matrix_divided(matrix, div):
    """Divide all item of matrix by div
    Argument: matrix is 2d list, div is the divisor"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
    row_size = len(matrix[0])
    for lis in matrix:
        if type(lis) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
        if row_size != len(lis):
            raise TypeError("Each row of the matrix must have the same size")
        row_size = len(lis)
        if type(lis) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
        for num in lis:
            if type(num) is not int and type(num) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")
        new = matrix[:]
        return list(map(
            lambda x: list(map(
                lambda y: round(y / 3, 2), x)), new))
