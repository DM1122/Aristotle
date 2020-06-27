"""
Updates all video entries in database. Does not reprocess video. Wrapper for requests to Video model.
"""

# stdlib
import os

# django
import django

# external
import cv2

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


def get_video_file(idd):
    """
    Download and return opended video file using youtubelibe and OpenCV. Ensures video exists in database, if not, adds it.
    
    Args:
        idd (str): Video idd in library
    
    Returns:
        video_file (OpenCV Video): Opened video file object
        file_data (dict): Video file metadata
    """
    print(f"[{script}]: Retrieving '{idd}' video file...") if verbosity >= 1 else None

    if idd not in get_stored_video_idds():
        raise ValueError(
            f"[{script}]: Did not find '{idd}' in library. Consider scouting metadata first."
        )

    file_data = youtubelib.download(idd=idd, path="tmp")
    file_path = "tmp/" + file_data["idd"] + ".mp4"

    video = cv2.VideoCapture(file_path)

    if not video.isOpened:
        raise Exception(f"[{script}]: Video file '{file_path}' could not be opened.")

    return video, file_data


# endregion
