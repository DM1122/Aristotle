"""
Memory consolidation. Visual & auditory memory.
"""

import os, sys

from components import scout, librarian, tagger, querier


script = os.path.basename(__file__)
verbosity = 3


def refresh():

    print(f"[{script}]: Refreshing Aristotle temporal lobe...")

    queries = querier.sampleSearchQueries(n=3)
    results = scout.expedition(queries=queries, search_sample_size=3, search_depth=1)


def setup():
    print(f"[{script}]: Setting up Aristotle temporal lobe...")

    print(f"[{script}]: Setup complete.")


if __name__ == "__main__":
    print(f"[{script}]: Run cortex entrypoint.")
