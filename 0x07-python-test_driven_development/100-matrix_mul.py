#!/usr/bin/python3
"""This module contains matrix_mul function"""


def matrix_mul(m_a, m_b):
    """Function that multiply 2 matrices"""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise TypeError("m_a can't be empty")
    if len(m_b) == 0:
        raise TypeError("m_b can't be empty")
    for i in m_a:
        if len(i) == 0:
            raise TypeError("m_a can't be empty")
    for i in m_b:
        if len(i) == 0:
            raise TypeError("m_b can't be empty")
    for i in m_a:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    row_size_m_a = len(m_a[0])
    for i in m_a[1:]:
        if len(i) != row_size_m_a:
            raise TypeError("each row of m_a must be of the same size")
    row_size_m_b = len(m_b[0])

    for i in m_b[1:]:
        if len(i) != row_size_m_b:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")
    all = []
    for i in range(len(m_a)):
        inner = []
        for j in range(len(m_b[0])):
            inner.append(0)
        all.append(inner)

    for a, lis in enumerate(m_a):
        for i, num in enumerate(lis):
            for k in range(len(m_b[0])):
                all[a][k] += num * m_b[i][k]
    return all
