#!/usr/bin/python3
"""Create a Rectangle"""


class Rectangle:
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Init Rectangle"""
        self.__width = width
        self.__height = height
        self.print_symbol = "#"
        self.shibaneo = "&"
        Rectangle.number_of_instances += 1
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if width < 0:
            raise ValueError("width must be >= 0")

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
    def height(self, value):
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
                    i += str(self.print_symbol)
                i += '\n'
            return i[:-1]

    def __repr__(self):
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
    
    @classmethod
    def square(cls, size=0): 
        """ square make"""
        return cls(size, size) 
