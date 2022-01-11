#!/usr/bin/python3
"""
POST an email #0
"""
import urllib.parse
import urllib.request
from sys import argv

if __name__ == '__main__':
    values = {'email': argv[2]}
    comp = urllib.parse.urlencode(values).encode('utf-8')
    request = urllib.request.Request(argv[1], comp)
    with urllib.request.urlopen(request) as r:
        print(r.read().decode('utf-8'))
