#!/usr/bin/python3
"""
Sends request to URL and displays value of
X-Request-Id variable found in header
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')

        if x_request_id:
            print(x_request_id)
