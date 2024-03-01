#!/bin/bash
# Sends a request to a URL and displays size in bytes

URL="$1"
curl -sI "$URL" | grep -i "Content-Length" | awk '{print $2}'

