#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """"List of integers"""
    if list_of_integers:
        return list_of_integers.sort(reverse=True)[0]
