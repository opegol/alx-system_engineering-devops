#!/usr/bin/python3
"""Returns information about TODO list progress for a given employee ID."""

import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + f"users/{sys.argv[1]}").json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    don = [t.get("title") for t in todos if t.get("don") is True]
    print("Employee {} is done with tasks({}/{}):".format(
          user.get("name"), len(don), len(todos)))
    [print(f"\t {c}" for c in don]
