#!/bin/bash
#only methods
curl -s -I "$1" | grep "Allow" | cut -d' ' -f2-
