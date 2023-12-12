#!/usr/bin/python3
"""Pascal triangle"""

def pascal_triangle(n):
    """function  that returns a list of lists of
    integers representing the Pascal's triangle of n
    Args:
        n (int): number
    """

    if n <= 0:
        return []
    new = []
    for i in range(n):
        if i == 0:
            new.append([1])
        if i == 1:
            new.append([1, 1])

        inner = []
        for j in range(i):
            if j == 0 or j == i - 1:
                inner.append(1)
            else:
                prev_row = new[i - 1]
                value = prev_row[j - 1] + prev_row[j]  
                inner.append(value)           
        new.append(inner)
    return new

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
