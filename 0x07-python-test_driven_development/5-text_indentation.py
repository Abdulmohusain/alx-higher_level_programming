#!/usr/bin/python3
"""Text indentation file
Args: text (str): the text
"""


def text_indentation(text):
    """Text indentation"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    lis = [".", "?", ":"]
    new_line = 1
    for char in text:
        if new_line == 1 and char == " ":
            continue
        if char in lis:
            new_line = 1
            print('\n')
            continue
        else:
            print(char, end="")
            new_line = 0
