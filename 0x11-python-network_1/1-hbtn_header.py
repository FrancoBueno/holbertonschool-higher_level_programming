#!/usr/bin/python3
"""
1. Response header value #0
"""

if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    with request.urlopen(argv[1]) as r:
        print(r.headers.get('X-Request-Id'))
