"""
Temporal lobe controller.

Responsible for memory consolidation, visual & auditory memory.
"""

# stdlib
import os
from pprint import pprint

# project
from components import librarian, querier, scout, tagger

script = os.path.basename(__file__)
verbosity = 3


def update():
    """
    Update lobe.
    """
    print(f"[{script}]: Updating temporal lobe...")

    queries = querier.sample_search_queries(n=3)
    datas = scout.expedition(queries=queries, search_size=3, search_depth=1)

    for data in datas:
        librarian.store_video_data(data=data)

    for video in librarian.get_video_library():
        tagger.apply_tags(video)

    print(f"[{script}]: Update complete.")


def setup():
    """
    Run component-level setup.
    """
    print(f"[{script}]: Setting up temporal lobe...") if verbosity >= 1 else None

    tagger.setup_tags()

    print(f"[{script}]: Set up complete.") if verbosity >= 2 else None


def inject(idd):
    """
    Add a specified video idd of interest into the library.
    
    Args:
        idd (str): YouTube video idd
    """
    metadata = scout.retrieve(idd=idd)
    librarian.store_video_data(data=metadata)
