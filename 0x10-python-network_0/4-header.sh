#!/bin/bash
# Takes in url as an argument and send GET request to the url
curl GET -sH "X-School-User-Id: 98" "$1"
