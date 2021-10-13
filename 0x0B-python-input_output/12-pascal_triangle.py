#!/usr/bin/python3
"""Pascal Exc 12"""


def pascal_triangle(n):
    """Pascal triangle """
    if n <= 0:
        return []

    C = []
    for columns in range(n):
        C.append([1])

        for i in range(1, columns):
            C[columns].append(C[columns - 1][i - 1] + C[columns - 1][C])

        if columns is not 0:
            C[columns].append(1)
        return C
