"""
Samples historical search queries to pass to scout.
"""

# stdlib
import os

# external
import numpy as np

# project
from library.models import SearchQuery

script = os.path.basename(__file__)
verbosity = 3


def sample_search_queries(n):
    """
    Sample common search queries from database.
    
    Args:
        n (int): number of queries to sample
    
    Returns:
        samples (list-str): list of sampled queries
    """
    print(f"[{script}]: Sampling search queries...") if verbosity >= 1 else None

    queries = []
    counts = []

    for e in SearchQuery.objects.all():
        queries.append(e.query)
        counts.append(e.count)

    if len(queries) == 0:
        print(f"[{script}]: WARNING: SearchQuery is empty.")
        return queries

    counts_total = sum(counts)
    probs = [x / counts_total for x in counts]

    n = len(queries) if n > len(queries) else n

    samples = list(np.random.choice(queries, size=n, replace=False, p=probs))

    print(f"[{script}]: Sampled.") if verbosity >= 2 else None

    return samples
