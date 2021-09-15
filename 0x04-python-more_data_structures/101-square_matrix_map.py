#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda f: list(map(lambda a: a ** 2, f)), matrix))
