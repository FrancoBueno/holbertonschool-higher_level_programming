#!/usr/bin/python3
""" write a string in a text file """


def write_file(filename="", text=""):
    """make file if not exist and write file """
    with open(filename, "w", encoding="utf-8") as Wfile:
        Wfile.write(text)
    return len(text)
