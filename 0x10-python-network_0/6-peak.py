#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """"List of integers"""
    if list_of_integers:
        peak = sorted(list_of_integers, reverse=True)[0]
        return peak
