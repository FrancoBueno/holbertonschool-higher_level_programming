#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    if len(argv) == 2:
        print("1 arguments:")
        print("1: {:s}".format(argv[1]))
    if len(argv) == 3:
        print("2 arguments:")
        print("1: {}".format(argv[1]))
        print("2: {}".format(argv[2]))
    if len(argv) == 4:
        print("3 arguments:")
        print("1: {}".format(argv[1]))
        print("2: {}".format(argv[2]))
        print("3: {}".format(argv[3]))
    if len(argv) == 5:
        print("4 arguments:")
        print("1: {}".format(argv[1]))
        print("2: {}".format(argv[2]))
        print("3: {}".format(argv[3]))
        print("4: {}".format(argv[4]))
    if len(argv) == 6:
        print("5 arguments:")
        print("1: {}".format(argv[1]))
        print("2: {}".format(argv[2]))
        print("3: {}".format(argv[3]))
        print("4: {}".format(argv[4]))
        print("5: {}".format(argv[5]))
    if len(argv) == 7:
        print("6 arguments:")
        print("1: {}".format(argv[1]))
        print("2: {}".format(argv[2]))
        print("3: {}".format(argv[3]))
        print("4: {}".format(argv[4]))
        print("5: {}".format(argv[5]))
        print("5: {}".format(argv[6]))
