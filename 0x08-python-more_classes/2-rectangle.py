#!/usr/bin/python3
"""define Rectangle"""


class Rectangle:
    """Rectangle"""
    def __init__(self, width=0, height=0):
        """Init Rectangle"""
        self.__width = width
        self.__height = height
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        elif isinstance(height, int) is False:
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")
        elif width < 0:
            raise ValueError("width must be >= 0")

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sadasdoasodaso"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self, value):
        """helapsapdaspd"""
        return self.__height

    @height.setter
    def height(self, value):
        """hasdiasdaishd"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ashdiasdhiasidasi"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * self.__height

    def perimeter(self):
        """asdjasodjaosdjas"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))
