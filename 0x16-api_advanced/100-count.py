#!/usr/bin/python3
"""Defines a recursive function that queries the Reddit API,
   parses the title of all hot articles, and prints a sorted
   count of given keywords.
 """

import requests


def count_words(subreddit, word_list, occr={}, after="", count=0):
    """prints a sorted count of given keywords found in
        hot posts of a given subreddit.
    """
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
        return

    res = res.get("data")
    after = res.get("after")
    count += res.get("dist")
    for child in res.get("children"):
        title = child.get("data").get("title").lower().split()
        for word in word_list:
            word = word.lower()
            if word in title:
                num = len([t for t in title if t == word])
                if occr.get(word) is None:
                    occr[word] = num
                else:
                    occr[word] += num

    if after is None:
        if len(occr) == 0:
            return
        occr = sorted(occr.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in occr:
            print(f"{k}: {v}")
    else:
        count_words(subreddit, word_list, occr, after, count)
