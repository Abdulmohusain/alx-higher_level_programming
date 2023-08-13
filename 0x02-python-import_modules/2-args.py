#!/usr/bin/python3
if __name__ == "__main__":
    import sys as sy
    if len(sy.argv) == 1:
        print("0 arguments.")
    elif len(sy.argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sy.argv) - 1))
    for i in sy.argv[1:]:
        print("{:d}: {:s}".format(sy.argv.index(i), i))
