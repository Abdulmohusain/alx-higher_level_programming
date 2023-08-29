#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ValueError:
        result = None
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {:.1f}".format(result))
        return result
