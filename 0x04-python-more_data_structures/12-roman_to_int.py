#!/usr/bin/python3
"""Roman to integer fucntion file"""


def roman_to_int(roman_string):
    """Roman to integer function"""

    if type(roman_string) is not str or roman_string is None:
        return 0

    integer_equivalent = 0

    


roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
