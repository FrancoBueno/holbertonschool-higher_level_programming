#!/usr/bin/python3
"""Raise exception based in the 5 excersice and area"""


class BaseGeometry:
    """Create instance """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checker me """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
