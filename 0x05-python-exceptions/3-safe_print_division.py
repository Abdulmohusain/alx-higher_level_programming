#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ValueError:
        result = None
    except ZeroDivisionError:
        result = None
    finally:
        if result:
            try:
                print("Inside result: {:d}".format(result))
            except ValueError:
                print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: None")
        return result
