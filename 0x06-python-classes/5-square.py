#!/usr/bin/python3
"""Hello EveryBody"""


class Square:
    """create Square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """size origin"""
        return self.__size

    @size.setter
    def size(self, value):
        """sett to size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return(self.__size ** 2)

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

