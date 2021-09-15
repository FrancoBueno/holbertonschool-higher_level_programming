#!/usr/bin/python3
def common_elements(set_1, set_2):
    listt = []
    for i in set_1:
        for f in set_2:
            if i == f:
                listt = i
                return listt
