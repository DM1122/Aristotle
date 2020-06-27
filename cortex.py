"""
Aristotle's brain. High-level delegation of tasks amongst lobe controllers.

All testing of lobe controllers and lower-level components must be done through cortex.

isort:skip_file
"""

# stdlib
import os
import sys
import time

# django
import django

sys.path.append("./arsite")  # must run before project imports
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arsite.settings")
django.setup()

# external
import schedule

# project
from lobes import frontal, occipital, parietal, temporal


script = os.path.basename(__file__)
verbosity = 3

lobes = [frontal, occipital, parietal, temporal]
update_freq = 0.5  # minutes


def main():
    """
    Autonomous operation.
    """
    print(f"[{script}]: Running Aristotle cortex...")

    setup()

    schedule.every(update_freq).minutes.do(update)

    while True:
        schedule.run_pending()
        time.sleep(1)


def update():
    """
    Update.
    """
    print(f"[{script}]: Updating cortex...")

    for lobe in lobes:
        lobe.update()

    print(f"[{script}]: Cortex update complete.")


def setup():
    """
    Configure lobes.
    """
    print(f"[{script}]: Setting up cortex...") if verbosity >= 1 else None

    for lobe in lobes:
        lobe.setup()

    print(f"[{script}]: Set up complete.") if verbosity >= 2 else None


if __name__ == "__main__":
    # main()
    occipital.update()
