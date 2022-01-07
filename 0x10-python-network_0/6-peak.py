#!/usr/bin/python3
# Find a peak

def find_peak(list_of_integers):
    i = 1 
    lista = list_of_integers
    if (not lista):
        return None
    if (len(lista) <= 2):
        maxvalue = max(lista)
        return maxvalue

    peak = None

    if lista[0] >= lista[1]:
        peak = lista[0]
    if lista[-1] >= lista[-2]:
        peak = lista[-1]
    if peak:
        return peak

    while(i < len(lista) -1):
        if lista[i] >= lista[i + 1] and lista[i] >= lista[i - 1]:
            return lista[i]
        else:
            i+=1
    return peak

