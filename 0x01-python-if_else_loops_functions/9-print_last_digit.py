#!/usr/bin/python3
def print_last_digit(number):
    lst = int(repr(number)[-1])
    print("{}".format(lst), end="")
    return lst
