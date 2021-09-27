#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    contador = 0
    for f in range (x):
        try:
            print("{:d}".format(my_list[f]), end="")
            contador += 1
        except (TypeError, ValueError):
            pass
    print()
    return contador
