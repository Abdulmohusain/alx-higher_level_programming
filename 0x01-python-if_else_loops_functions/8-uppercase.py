#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 96 and ord(i) <= 122:
            j = ord(i) - 32
            print("{:c}".format(j), end="")
    print("")

