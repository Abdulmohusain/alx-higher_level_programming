#!/usr/bin/python3
for i in range(97, 123):
    if ord('q') == i or i == ord('e'):
        continue
    print("{:c}".format(i), end="")
