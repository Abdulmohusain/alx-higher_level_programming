#!/usr/bin/python3
"""Weighted average"""


def weight_average(my_list=[]):
    """Average"""

    if type(my_list) is not list or len(my_list) == 0:
        return 0
    quotient = 0
    divisor = 0
    for i in range(len(my_list)):
        quotient += my_list[i][0] * my_list[i][1]
        divisor += my_list[i][1]
    return quotient / divisor
