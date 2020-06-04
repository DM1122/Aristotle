"""
Parses entire database and applies tags according to Video metadata.
"""

import os, sys


# sys.path.append('./arsite')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arsite.settings')
# import django
# django.setup()
# from library.models import Tag, Video, SearchQuery
# from libs import youtubelib
# import numpy as np
# from pprint import pprint

# from datetime import datetime

script = os.path.basename(__file__)
verbosity = 3


tags = [  # the definitive list of available tags
    "New",
    "Credible",
    "Interactive",
    "Personal",
    "Paper & Pencil",
    "Silent",
    "Text",
    "Animated",
    "HD",
    "Popular",
    "Quick",
    "Lecture",
]


date_format = "%Y/%m/%d"


def createTags():
    print(f"[{script}]: Creating tags...") if verbosity >= 1 else None

    # get current tags in database to avoid duplication
    tags_current = [x.name for x in Tag.objects.all()]

    for tag in tags:
        if tag in tags_current:
            print(
                f'[{script}]: WARNING: "{tag}" already in database. Ignoring.'
            ) if verbosity >= 3 else None
        else:
            Tag(name=tag).save()
            print(f'[{script}]: Added "{tag}".') if verbosity >= 3 else None

    print(f"[{script}]: Tag creation complete.") if verbosity >= 2 else None


def clearTags():
    """
    Clears the database of all tags.
    """
    print(f"[{script}]: Clearing tags from database.") if verbosity >= 1 else None

    for tag in Tag.objects.all():
        tag.delete()
        print(f'[{script}]: Removed "{tag}" tag.') if verbosity >= 3 else None

    print(f"[{script}]: Done clearing database tags.") if verbosity >= 2 else None


def clearVideoTags():
    """
    Clears all tags from all videos in database.
    """

    print(f"[{script}]: Clearing tags from all videos.") if verbosity >= 1 else None

    for video in Video.objects.all():
        video.tags.clear()
        print(f'[{script}]: Cleared tags from "{video}".') if verbosity >= 3 else None

    print(f"[{script}]: Done clearing video tags.") if verbosity >= 2 else None


def applyTag(name, video):
    """
    Applies a given tag to a given video.
    """
    if name not in tags:
        raise ValueError(f'[{script}]: Tag "{tag}" does not exist in database.')

    tag = Tag.objects.get(name=name)
    video.tags.add(tag)
    print(f'[{script}]: Applied "{tag}" tag to "{video}".') if verbosity >= 2 else None


# def applyTags(video):
#     '''
#     Contains all the logic for choosing which tags to apply based on video metadata.
#     '''
#     print(f'[{script}]: Applying tags to "{video}"...') if verbosity>=1 else None


#     result = checkTagNew(video)

#     print(f'[{script}]: Done application to "{video}".') if verbosity>=2 else None


def checkTagNew(video):
    """
    Determines whether {tag} is applicable and if so, applies tag.
    """
    delta = video.updated.date() - video.published

    flag = True if delta.days <= 30 else False

    if flag:
        applyTag("New", video)


def checkTagQuick(video):
    """
    Determines whether {tag} is applicable and if so, applies tag.
    """
    flag = True if video.duration <= 90 else False

    if flag:
        applyTag("Quick", video)


if __name__ == "__main__":
    print(f"[{script}]: Run cortex entrypoint.")

    # clearVideoTags()

    # for video in Video.objects.all():
    #     print(video.tags.name)
    #     # checkTagNew(video)
    #     # checkTagQuick(video)

    # print(f'[{script}]: Tag job complete.')
