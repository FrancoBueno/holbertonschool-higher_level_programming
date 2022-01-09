#!/bin/bash
#ends a request to a URL passed as an argument
curl "$1" -so /dev/null -w "%{http_code}"
