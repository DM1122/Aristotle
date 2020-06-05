"""
Updates all video entries in database. Does not reprocess video. Wrapper for requests to Video model.
"""

# stdlib
import os

# django
import django

# project
from library.models import Video
from libs import youtubelib

script = os.path.basename(__file__)
verbosity = 3


def store_video_data(data):
    """
    Update video entry or creates new video entry in library if one does not exist.
    """
    data["updated"] = django.utils.timezone.now()
    video, created = Video.objects.update_or_create(idd=data["idd"], defaults=data)

    if created:
        print(
            f'[{script}]: Added "{video.idd}" data to library!'
        ) if verbosity >= 3 else None
    else:
        print(f'[{script}]: Updated "{video.idd}" data!') if verbosity >= 3 else None


def housekeeping():
    """
    Update the entire video library metadata. Does not update tags.
    """
    print(f"[{script}]: Conducting housekeeping...")

    for video in Video.objects.all():
        data = youtubelib.getYTVideoData(idd=video.idd)
        store_video_data(data)

    print(f"[{script}]: Housekeeping complete.")


# region helpers
def get_stored_video_idds():
    """
    Return a list of all currently stored video idds from database.
    """
    idds = [video.idd for video in Video.objects.all()]

    return idds


def get_video_data(idd):
    """
    Return video obj from library according to idd.
    """
    video = Video.objects.get(idd=idd)

    return video


def clear_video_library():
    """
    Wipes entire video library.
    """
    print(f"[{script}]: Clearing video library.")

    for video in get_video_library():
        video.delete()
        print(f'[{script}]: Removed "{video}".') if verbosity >= 3 else None

    print(f"[{script}]: Cleared video library.")


def get_video_library():
    """
    Retrieve all video data in library.
    """
    return Video.objects.all()


# endregion
