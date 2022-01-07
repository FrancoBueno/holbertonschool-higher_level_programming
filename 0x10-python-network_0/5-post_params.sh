#!/bin/bash
#POST parameters

curl -sX "$1" POST -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD'
