#!/usr/bin/python3
"""
Sends POST request to URL with an email parameter and
displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)
