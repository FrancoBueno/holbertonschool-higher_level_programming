#!/usr/bin/python3
"""the class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle that inherit from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width self"""
        return self.__width

    @width.setter
    def width(self, value):
        """width for output"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height self """
        return self.__height

    @height.setter
    def height(self, value):
        """height output"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ x Output"""
        return self.__x

    @x.setter
    def x(self, value):
        """ X of the imput"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """ Y self """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y of the imput """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """area of rectangle """
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle character # """
        for a in range(self.__y):
            print("")
        for i in range(self.__height):
            for n in range(self.__x):
                print(" ", end="")
            for f in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Function that return id and parameters"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
