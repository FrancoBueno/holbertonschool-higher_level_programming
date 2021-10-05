#!/usr/bin/python3
""" sum of integrers """


def add_integer(a, b=98):
    """
    the function add two integrals with arguments,
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    a = int(a)
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    b = int(b)

    return a + b
