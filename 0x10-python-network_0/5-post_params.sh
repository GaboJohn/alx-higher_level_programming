#!/bin/bash
# Takes in url send a POST request to the passed url
curl -s POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
