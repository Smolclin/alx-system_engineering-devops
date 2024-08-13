#!/usr/bin/python3
""" import requests modules """

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers) 
    or a given subreddit. If an invalid subreddit is given,
    the function should return 0"""

    headers = {'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    url = "https://www.reddit.com/r/{}/about".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
