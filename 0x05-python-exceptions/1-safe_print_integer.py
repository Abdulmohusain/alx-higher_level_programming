#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        value = int(value)
        return True
    except Exception:
        return False
