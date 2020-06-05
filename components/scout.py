"""
Takes care of searching Youtube according to relevant key terms from database and returns video info to database.
"""

# stdlib
import os

# project
from libs import youtubelib

script = os.path.basename(__file__)
verbosity = 3


def expedition(queries, search_size=3, search_depth=1):
    """
    Search youtube for relevant videos according to popular search queries in database.

    Args:
        queries (list): list of query strings
        search_size (int): number of video results to parse
        search_depth (int): Number of recursion steps to get videos related to search results. WIP

    Returns:
        datas (list-dict): list of video metadata dicts
    """
    print(f"[{script}]: Conducting expedition...")

    for query in queries:
        ids = youtubelib.searchYT(query=query, maxResults=search_size)

        datas = []
        for idd in ids:
            data = youtubelib.getYTVideoData(idd=idd)

            datas.append(data)

    print(f"[{script}]: Expedition complete.")

    return datas
