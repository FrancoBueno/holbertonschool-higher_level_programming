#!/usr/bin/python3
"""Function that read File"""


def read_file(filename=""):
    """open and read and print file"""
    with open(filename, "r", encoding="utf-8") as rfile:
        print(rfile.read(), end="")
