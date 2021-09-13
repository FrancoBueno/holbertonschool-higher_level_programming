#!/usr/bin/env python3
def no_c(my_string):
    print(my_string.translate({ord('c'): None}))
    print(my_string.translate({ord('C'): None}))
    return(my_string)
