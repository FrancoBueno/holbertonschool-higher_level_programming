#!/usr/bin/python3
"""madre mia willi"""


class Square:
    """Hoasdasd alasdas """
    def __init__(self, size=0, position=(0, 0)):
        """Measdas"""
        self.__size = size
        self.position = position
 
    @property
    def size(self):
        """newaeadsad adasd"""
        return self.__position
    
    @property
    def position(self):
        """ahdahsdh"""
        return self.__position

    @size.setter
    def size(self, value):
        """Heallsadoasod """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """HEALDSADOAS"""
        if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or value[0] < 0 or \
            type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    
    def area(self):
        """Headasd asasda"""
        return(self.__size ** 2)

    def my_print(self):
        """asdasdasd """
        if self.__size == 0:
            print()
        else:
            for l in range(self.__position[1]):
                print()
            for i in range(self.__position[1]):
                print(" ", end="")
            for a in range(self.__position[0]):
                print("#", end="")
            print()

