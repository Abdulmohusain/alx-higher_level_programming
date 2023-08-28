#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if type(my_list) is not list:
        return 0
    j = 0
    k = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            j += 1
        except TypeError:
            continue
        except ValueError:
            continue
        finally:
            k += 1
            if k == x:
                break
    print("")
    return j
