#!/usr/bin/python3
def remove_char_at(str, n):
    """ A function that removes an item the c way"""
    if n < 0:
        return str
    string = str[:n] + str[n+1:]
    return string
