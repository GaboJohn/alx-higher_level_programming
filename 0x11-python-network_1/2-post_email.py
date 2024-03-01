#!/usr/bin/python3
"""
Sends POST request to URL with email parameter.
"""

import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        return response.read().decode('utf-8')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response_content = send_post_request(url, email)
    print(response_content)
