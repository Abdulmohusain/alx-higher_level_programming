
#!/usr/bin/python3
"""Multiply"""


def multiply_by_2(a_dictionary):
    """multiply by 2"""

    if type(a_dictionary) is not dict:
        return
    new = a_dictionary.copy()
    for key, value in new.items():
        new[key] = value * 2
    return new
