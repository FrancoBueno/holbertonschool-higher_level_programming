#!/bin/usr/python3
def search_replace(my_list, search, replace):
    listeana = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    for i in listeana:
        if listeana[i] == 2:
            listeana.insert(i, 89)
        return listeana
