"""
Updates all video entries in database. Does not reprocess video. Wrapper for requests to Video model.
Will run on command, as well as when video is sent to display.
"""

import os, sys

# sys.path.append('arsite')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arsite.settings')
# import django
# django.setup()

# from library.models import *
# from django.utils import timezone

# # from temporal import *
# # sys.path.append('/Aristotle')
# from .. import libs

# import numpy as np
# from pprint import pprint


script = os.path.basename(__file__)
verbosity = 3


def main():
    print(f"[{script}]: Running Librarian...")


def storeVideoData(data):
    """
    Updates video entry or creates new video entry in library if one does not exist.
    """

    data["updated"] = timezone.now()
    video, created = Video.objects.update_or_create(idd=data["idd"], defaults=data)

    if created:
        print(
            f'[{script}]: Added "{video.idd}" data to library!'
        ) if verbosity >= 3 else None
    else:
        print(f'[{script}]: Updated "{video.idd}" data!') if verbosity >= 3 else None


def housekeeping():
    """
    Updates the entire video library metadata. Should call tagger afterwards.
    """

    print(f"[{script}]: Conducting housekeeping...")

    for video in Video.objects.all():
        data = youtubelib.getYTVideoData(idd=video.idd)
        storeVideoData(data)

    print(f"[{script}]: Housekeeping complete.")


# region helpers
def getStoredVideoIdds():
    """
    Returns a list of all currently stored video idds from database.
    """

    idds = [video.idd for video in Video.objects.all()]

    return idds


def getVideoMetadata(idd):
    """
    Returns video obj from library according to idd.
    """

    video = Video.objects.get(idd=idd)

    return video


def clearVideoLibrary():
    """
    Wipes entire video library.
    """

    print(f"[{script}]: Clearing video library.")

    for video in getVideoLibrary():
        video.delete()
        print(f'[{script}]: Removed "{video}".') if verbosity >= 3 else None

    print(f"[{script}]: Cleared video library.")


def getVideoLibrary():
    """
    Retrives all video data in library.
    """

    return Video.objects.all()


# endregion


if __name__ == "__main__":
    print(f"[{script}]: Run cortex entrypoint.")

    # pprint(sys.path)
    # print()
    # pprint(os.environ)

    # housekeeping()
