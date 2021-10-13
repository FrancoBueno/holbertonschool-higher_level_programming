#!/usr/bin/python3
"""Raise exception based in the 5 excersice and area"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """New Class Square That Print The size """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return(self.__size * self.__size)

    def __str__(self):
        return("[Square] {}/{}".format(self.__size, self.__size))
