#!/usr/bin/python3
""" NOT TO JUANJIS """


def matrix_divided(matrix, div):
    """created Class"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    
    listnew = []
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        listout = []
        for f in i:
            if type(f) is not int and type(f) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                return 
            listout.append(round(f / div, 2))
        listnew.append(listout)
    return listnew
