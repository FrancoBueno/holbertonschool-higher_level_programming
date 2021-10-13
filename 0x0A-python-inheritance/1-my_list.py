#!/usr/bin/python3
""" function that create list and sort the list"""
class MyList(list):
    """My list new"""
    def print_sorted(self):
        print(sorted(self))
