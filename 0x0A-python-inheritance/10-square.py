#!/usr/bin/python3
"""Raise exception based in the 5 excersice and area"""
Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """New Class Square That Print The size """
    def __init__(self, size):
        try:
            self.integer_validator("size", size)
            super().__init__(size, size)
        except Exception as e:
            raise e

