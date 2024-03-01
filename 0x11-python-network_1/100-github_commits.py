#!/usr/bin/python3
"""
Lists 10 commits of a GitHub repository by a specified user.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = (
            f'https://api.github.com/repos/{owner_name}/'
            f'{repository_name}/commits'
            )

    params = {'per_page': 10}
    response = requests.get(url, params=params)

    try:
        data = response.json()
        for commit in data:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    except ValueError:
        print("Not a valid JSON")
