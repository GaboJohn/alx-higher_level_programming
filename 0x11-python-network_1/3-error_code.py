#!/usr/bin/python3
"""
Sends request to URL and displays the body of the response.
"""

import urllib.request
import urllib.error
import sys


def fetch_and_display(url):
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_and_display(url)
