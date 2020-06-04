import os, sys

sys.path.append("./arsite")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arsite.settings")
import django

django.setup()

# from library.models import SearchQuery

import schedule
import time

from lobes import frontal, occipital, parietal, temporal


script = os.path.basename(__file__)
verbosity = 1


def main():
    print(f"[{script}]: Running Aristotle cortex...")

    temporal.setup()

    schedule.every(1).minutes.do(temporal.refresh())

    while True:
        schedule.run_pending()
        time.sleep(1)


def test():
    temporal.refresh()


if __name__ == "__main__":
    test()
