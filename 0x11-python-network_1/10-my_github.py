#!/usr/bin/python3
"""
Uses the GitHub API to display your id using Basic Authentication
with a personal access token.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./9-github_identity.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, token))

    try:
        data = response.json()
        print(data.get('id'))
    except ValueError:
        print("Not a valid JSON")
