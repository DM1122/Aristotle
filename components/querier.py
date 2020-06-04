"""
Samples historical search queries to pass to scout.
"""

import os, sys
import numpy as np

from library.models import SearchQuery


script = os.path.basename(__file__)
verbosity = 3


def sampleSearchQueries(n):
    """
    Samples queries to be searched from searchQuery model according to popularity.
    n: query sample size
    """

    print(f"[{script}]: Sampling search queries...") if verbosity >= 1 else None

    queries = list()
    counts = list()

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


if __name__ == "__main__":
    print(f"[{script}]: Run cortex entrypoint.")
