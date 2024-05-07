#!/usr/bin/python3
"""Defines function that queries the Reddit API and returns the
   number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
                "User-Agent": "ubuntu:alx.0x16.api:v1.0.0 (by /u/ezekmanny)"
                }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    res = response.json().get("data")
    return res.get("subscribers")
