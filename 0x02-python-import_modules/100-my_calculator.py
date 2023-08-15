#!/usr/bin/python3
if __name__ == "__main__":
    import sys as sy
    import calculator_1 as cal

    arg = sy.argv
    if len(arg) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op_list = ["+", "-", "*", "/"]
    a = int(arg[1])
    o = arg[2]
    b = int(arg[3])
    if o not in op_list:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if o == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, o, b, cal.add(a, b)))
    if o == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, o, b, cal.sub(a, b)))
    if o == "*":
        print("{:d} {:s} {:d} = {:d}".format(a, o, b, cal.mul(a, b)))
    if o == "/":
        print("{:d} {:s} {:d} = {:d}".format(a, o, b, cal.div(a, b)))
