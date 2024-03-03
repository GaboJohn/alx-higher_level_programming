#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -sIX OPTIONS "$1" | grep -i 'allow' | cut -d ' ' -f 2-
