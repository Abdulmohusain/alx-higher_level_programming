#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as ab
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, ab.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, ab.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, ab.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, ab.div(a, b)))
