#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = []
    for x in matrix:
        nmatrix.append(list(map(lambda x: x**2, x)))
    return nmatrix
