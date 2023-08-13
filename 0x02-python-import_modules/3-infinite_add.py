#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument_list = sys.argv
    if len(argument_list) == 1:
        print(0)
    else:
        result = 0
        for i in argument_list[1:]:
            result += int(i)
        print("{:d}".format(result))
