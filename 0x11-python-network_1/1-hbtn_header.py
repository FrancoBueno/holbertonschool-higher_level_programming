#!/usr/bin/python3
import urllib.request as request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as r:
        print(r.headers.get('X-Request-Id'))
