#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupa = tuple_a or(0, 0)
    tupb = tuple_b or(0, 0)
    if len(tuple_a) == 1:
        tupa = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        tupb = (tuple_b[0], 0)
    return(tupa[0] + tupb[0], tupa[1] + tupb[1])
