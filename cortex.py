"""
Aristotle's brain. High-level delegation of tasks amongst lobe controllers.

All testing of lobe controllers and lower-level components must be done through cortex.
"""

# stdlib
import os
import sys
import time

# django
import django

# external
import schedule

# project
from lobes import frontal, occipital, parietal, temporal

sys.path.append("./arsite")  # must run before application imports
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arsite.settings")
django.setup()


script = os.path.basename(__file__)
verbosity = 3

lobes = [frontal, occipital, parietal, temporal]


def main():
    """
    Run main.
    """
    print(f"[{script}]: Running Aristotle cortex...")

    setup()

    temporal.update()

    # schedule.every(1).minutes.do(temporal.refresh())

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)


def setup():
    """
    Configure lobes.
    """
    print(f"[{script}]: Setting up cortex...") if verbosity >= 1 else None

    for lobe in lobes:
        lobe.setup()

    print(f"[{script}]: Set up complete.") if verbosity >= 2 else None


if __name__ == "__main__":
    main()
