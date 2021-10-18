#!/usr/bin/python3
"""10. And now, the Square!"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square that inherit Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """return the arguments of square"""
        if self.width == 0 and self.height == 0:
            return
        else:
            return("[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """default size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary Rectangle """

        return ({"id": self.id, "x": self.x, "size": self.size, "y": self.y})
