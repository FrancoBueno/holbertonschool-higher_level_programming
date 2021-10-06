#!/usr/bin/python3
"""Print Square Fast"""


def print_square(size):
    """create deff"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
