#!/usr/python3

"""  function that queries the Reddit API and returns
a list containing the titles of all hot articles for
a given subreddit. If no results are found for the
given subreddit, the function should return """


def recurse(subreddit, hot_list=[], after=None):
    """ function that queries the Reddit API """
    import requests

    info = requests.get("https://www.reddit.com/r/{}/hot.json"
                        .format(subreddit),
                        params={"count": count, "after": after},
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if info.status_code >= 400:
        return None

    hot_1 = hot_list + [child.get("data").get("title")
                        for child in info.json()
                        .get("data")
                        .get("children")]

    inf = info.json()
    if not inf.get("data").get("after"):
        return hot_1

    return recurse(subreddit, hot_1, inf.get("data").get("count"),
                   inf.get("data").get("after"))
