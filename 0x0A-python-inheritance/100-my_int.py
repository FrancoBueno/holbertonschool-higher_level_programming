#!/usr/bin/python3
""" 100 Advanced task"""

class MyInt(int):
    """clas new"""
    def __eq__(self, value):
        return not super().__eq__(value)
    def __ne__(self, value):
        return not super().__ne__(value)
