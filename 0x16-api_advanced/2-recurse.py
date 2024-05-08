#!/usr/bin/python3
"""Recursive function that queries the Reddit API and
   returns a list containing the titles of all hot
   articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
                "User-Agent": "ubuntu:alx.0x16.api:v1.0.0 (by /u/ezekmanny)"
                }
    params = {
                "after": after,
                "count": count,
                "limit": 100
                }
    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    try:
        res = resp.json()
        if resp.status_code == 404:
            raise Exception
    except Exception:
        return None

    res = res.get("data")
    after = res.get("after")
    count += res.get("dist")
    for child in res.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
