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

class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
    def area(self):
        return(self.__width * self.__height)
    def __str__(self):
        """Return str """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

class Square(Rectangle):
    def __init__(self, size):
        try:
            self.integer_validator("size", size)
            super().__init__(size, size)
        except Exception as e:
            raise e

