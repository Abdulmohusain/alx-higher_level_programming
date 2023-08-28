#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if type(my_list) != list:
        return 0
    j = 0
    k = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            j += 1
        except TypeError:
            continue
        except IndexError:
            continue
        finally:
            k += 1
            if k == x:
                break
    print("")
    return j









my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
