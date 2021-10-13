#!/usr/bin/python3
"""Rewadasd"""


def append_write(filename="", text=""):
    """Append strings to file or new file """
    with open(filename, "a", encoding="utf-8") as Afile:
        Afile.write(text)
        return len(text)
