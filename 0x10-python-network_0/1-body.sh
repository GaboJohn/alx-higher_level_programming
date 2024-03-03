#!/bin/bash
# Sends a GET request to a URL and displays the body of the response for a 200 status code

URL="$1"
curl -s -L "$URL"

