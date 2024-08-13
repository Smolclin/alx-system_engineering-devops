#!/usr/bin/python3
""" import requests modules """

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers) 
    or a given subreddit. If an invalid subreddit is given,
    the function should return 0"""

    headers = {'User-Agent': 'CustomClient/1.0'}
    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return (0)
    response = response.json()
    if 'data' in response:
        return (response.get('data').get(subscribers))

    else:
        return (0)
