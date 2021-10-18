#!/usr/bin/python3
"""10. And now, the Square!"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square that inherit Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """default size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size"""
        setattr(self, "width", value)
        setattr(self, "height", value)

    def __str__(self):
        """return the arguments of square"""
        return("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
            else:
                for key, value in kwargs.items():
                    setattr(self, "key", value)
