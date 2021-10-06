#!/usr/bin/python3
"""Create a Rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Init Rectangle"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must  be >= 0")
        else:
            self.__width = width
        if type(height, int) is not int:
            raise TypeError("heigth must be an integer")
        elif height < 0:
            raise ValueError("height must be an integer")
        else:
            self.__height = height
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        i = ""
        if self.__width == 0 or self.__height == 0:
            return i
        else:
            for larg in range(self.__height):
                for col in range(self.__width):
                    i += '#'
                i += '\n'
            return i[:-1]
