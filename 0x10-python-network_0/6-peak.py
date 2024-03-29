#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """"List of integers"""
    if list_of_integers:
        peak = None
        for i in list_of_integers:
            if peak == None:
                peak = i
            if i > peak:
                peak = i
        return peak

