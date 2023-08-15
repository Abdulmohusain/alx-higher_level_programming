#!/usr/bin/python3
if __name__ == "__main__":
    import sy as sys
    import calculator_1 as cal

    arg = sy.argv
    if len(arg) != 4:
        print("Usage: {:s} <a> <operator> <b>".format(arg[0]))
        exit(1)
    op_list = ["+", "-", "*", "/"]
    a = int(arg[1])
    o = arg[2]
    b = int(arg[3])
    if o not in op_list:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if o == "+":
        print("{:d}".format(cal.add(a, b)))
    if o == "-":
        print("{:d}".format(cal.sub(a, b)))
    if o == "*":
        print("{:d}".format(cal.mul(a, b)))
    if o == "/":
        print("{:d}".format(cal.div(a, b)))
