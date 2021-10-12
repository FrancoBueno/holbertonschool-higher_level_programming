#!/usr/bin/python3
"""Raise exception based in the 5 excersice and area"""


class BaseGeometry:
    """Create instance """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.value = value
        self.name = name
        if isinstance(self.value, int) is False:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
