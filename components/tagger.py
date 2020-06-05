"""
Parses entire database and applies tags according to Video metadata.
"""

# stdlib
import os

# project
from library.models import Tag, Video

script = os.path.basename(__file__)
verbosity = 3

TAG_LIST = [  # the definitive list of available tags
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


def apply_tags(video):
    """
    Apply relevant tags to video according to metadata.
    
    Args:
        video (Video): video object in database
    """
    print(f"[{script}]: Applying tags to {video}...") if verbosity >= 1 else None

    check_list = [check_tag_new, check_tag_quick]

    for check in check_list:
        tag, flag = check(video=video)
        if flag:
            apply_tag(name=tag, video=video)
        else:
            print(
                f"[{script}]: Skipped '{tag}' on '{video.idd}'."
            ) if verbosity >= 3 else None

    print(f"[{script}]: Applied tags.") if verbosity >= 2 else None


# region Helpers
def apply_tag(name, video):
    """
    Apply specified tag to video.
    
    Args:
        name (str): tag name
        video (Video): video object in database
    """
    if name not in TAG_LIST:
        raise ValueError(f'[{script}]: Tag "{name}" does not exist in database!')

    tag = Tag.objects.get(name=name)
    video.tags.add(tag)

    print(f'[{script}]: Applied "{tag}" tag to "{video}".') if verbosity >= 2 else None


def setup_tags():
    """
    Instatiate tags from TAG_LIST into database.

    Does not clear previous tags to prevent video tag reference loss.

    TODO: remove tags that are not listed in TAG_LIST
    """
    print(f"[{script}]: Setting up tags...") if verbosity >= 1 else None

    # get current tags in database to avoid duplication
    tags_current = [x.name for x in Tag.objects.all()]

    for tag in TAG_LIST:
        if tag in tags_current:
            print(
                f'[{script}]: WARNING: "{tag}" already in database. Ignoring.'
            ) if verbosity >= 3 else None
        else:
            Tag(name=tag).save()
            print(f'[{script}]: Added "{tag}".') if verbosity >= 3 else None

    print(f"[{script}]: Tag creation complete.") if verbosity >= 2 else None


def clear_all_tags():
    """
    Clear the database of all tags.
    """
    print(
        f"[{script}]: Clearing tags from library database."
    ) if verbosity >= 1 else None

    for tag in Tag.objects.all():
        tag.delete()
        print(f'[{script}]: Removed "{tag}" tag.') if verbosity >= 3 else None

    print(f"[{script}]: Done clearing database tags.") if verbosity >= 2 else None


def clear_all_video_tags():
    """
    Clear all tags from all videos in database.
    """
    print(f"[{script}]: Clearing tags from all videos.") if verbosity >= 1 else None

    for video in Video.objects.all():
        video.tags.clear()
        print(f'[{script}]: Cleared tags from "{video}".') if verbosity >= 3 else None

    print(f"[{script}]: Done clearing video tags.") if verbosity >= 2 else None


# endregion


# region Checks
def check_tag_new(video):
    """
    Determine if tag 'New' is applicable.
    
    Args:
        video (Video): video object in database

    Returns:
        tag (str): tag to be applied
        flag (bool): whether or not to apply tag
    """
    tag = "New"

    delta = video.updated.date() - video.published

    flag = True if delta.days <= 30 else False

    return tag, flag


def check_tag_quick(video):
    """
    Determine if tag 'Quick' is applicable.
    
    Args:
        video (Video): video object in database

    Returns:
        tag (str): tag to be applied
        flag (bool): whether or not to apply tag
    """
    tag = "Quick"

    flag = True if video.duration <= 90 else False

    return tag, flag


# endregion
