#!/usr/bin/python3
"""Defines a function that queries the Reddit API and prints the
   titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed
       for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
                "User-Agent": "ubuntu:alx.0x16.api:v1.0.0 (by /u/ezekmanny)"
                }
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        res = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("None")
        return
    res = res.get("data")
    for child in res.get("children"):
        print(child.get("data").get("title"))
