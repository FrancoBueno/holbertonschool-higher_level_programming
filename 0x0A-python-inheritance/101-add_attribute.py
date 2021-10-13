#!/usr/bin/python3
""" Module New Attribute"""


def add_attribute(obj, name, value):
    """ new attribute """

    if hasattr(obj, '__dict__') is True:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
