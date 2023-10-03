"""Module contains print_square functions
A  function that prints a square with the character #.
"""


def print_square(size):
    """function that prints a square with
    the character #
    Args:
        size (int): size of square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
        return

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
