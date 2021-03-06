"""Wrapper for youtube api requests."""

# stdlib
import os
from datetime import datetime
from pprint import pprint

# external
import isodate
import pytube
from decouple import config
from googleapiclient.discovery import build

script = os.path.basename(__file__)
verbosity = 3
API_KEY = config("API_YOUTUBE_KEY")


def search(query, max_results=16):
    """
    Return list of relevant YT video ids.
    """
    print(f'[{script}]: Searching YT for "{query}"...') if verbosity >= 1 else None

    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.search().list(
        part="id",
        channelId=None,
        channelType=None,
        eventType=None,
        forContentOwner=None,
        forDeveloper=None,
        forMine=None,
        location=None,
        locationRadius=None,
        maxResults=max_results,
        onBehalfOfContentOwner=None,
        order=None,
        pageToken=None,
        publishedAfter=None,
        publishedBefore=None,
        q=query,
        regionCode=None,
        relatedToVideoId=None,
        relevanceLanguage=None,
        safeSearch=None,
        topicId=None,
        type="video",
        videoCaption=None,
        videoCategoryId=None,
        videoDefinition=None,
        videoDimension=None,
        videoDuration=None,
        videoEmbeddable=None,
        videoLicense=None,
        videoSyndicated=None,
        videoType=None,
    )
    response = request.execute()

    ids = [item["id"]["videoId"] for item in response["items"]]

    print(f"[{script}]: YT search complete.") if verbosity >= 2 else None
    return ids


def get(idd):
    """
    Return dict containing video metadata of interest from given id.
    """
    print(f'[{script}]: Collecting data for "{idd}"...') if verbosity >= 1 else None

    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.videos().list(
        part="snippet, contentDetails, statistics",
        chart=None,
        hl=None,
        id=idd,
        locale=None,
        maxHeight=None,
        maxResults=None,
        maxWidth=None,
        myRating=None,
        onBehalfOfContentOwner=None,
        pageToken=None,
        regionCode=None,
        videoCategoryId=None,
    )
    response = request.execute()
    response = response["items"][0]

    data = {
        "title": response["snippet"]["title"],
        "idd": idd,
        "thumbnail": response["snippet"]["thumbnails"]["default"]["url"],
        "author": response["snippet"]["channelTitle"],
        "published": datetime.strptime(
            response["snippet"]["publishedAt"], "%Y-%m-%dT%H:%M:%S%z"
        ),
        "description": response["snippet"]["description"],
        "duration": isodate.parse_duration(
            response["contentDetails"]["duration"]
        ).total_seconds(),
        "views": response["statistics"]["viewCount"],
    }

    try:
        data["rating"] = int(response["statistics"]["likeCount"]) / (
            int(response["statistics"]["likeCount"])
            + int(response["statistics"]["dislikeCount"])
        )
    except KeyError:
        print(
            f'[{script}]: WARNING: "{idd}" does not have ratings enabled.'
        ) if verbosity >= 2 else None
        data["rating"] = -1

    try:
        data["comment_count"] = response["statistics"]["commentCount"]
    except KeyError:
        print(
            f'[{script}]: WARNING: "{idd}" does not have comments enabled.'
        ) if verbosity >= 2 else None
        data["comment_count"] = -1

    print(f"[{script}]: Got video data.") if verbosity >= 2 else None
    return data


def download(idd, path):
    """
    Download video to path and returns the stream data.
    """
    print(f'[{script}]: Downloading YT video "{idd}"...') if verbosity >= 1 else None

    try:
        yt = pytube.YouTube("https://www.youtube.com/watch?v=" + idd)
        stream = yt.streams.filter(progressive=True).first()
        stream.download(path, filename=idd)
    except Exception:
        print(f'[{script}]: Failed download of YT video "{idd}".')
        return None

    data = {
        "idd": idd,
        "abr": stream.abr,
        "acodec": stream.audio_codec,
        "bitrate": stream.bitrate,
        "codecs": stream.codecs,
        "fps": stream.fps,
        "mime": stream.mime_type,
        "res": stream.resolution,
        "vcodec": stream.video_codec,
        "size": stream._filesize,
        "frames": stream.fps * yt.length,
    }

    file_path = path + "/" + data["idd"] + ".mp4"
    print(
        f'[{script}]: Download successful. Saved to "{file_path}".'
    ) if verbosity >= 2 else None
    return data


if __name__ == "__main__":
    print(f"[{script}]: Running tests...")
    case = 0

    if case == 0:
        print(f"[{script}]: Running test case {case}...")

        result = search(query="Never gonna", maxResults=16)

        print("Result:")
        pprint(result)
        print(f"[{script}]: Test case {case} complete.")

    elif case == 1:
        print(f"[{script}]: Running test case {case}...")

        result = get(idd="dQw4w9WgXcQ")

        print("Result:")
        pprint(result)
        print(f"[{script}]: Test case {case} complete.")

    elif case == 2:
        print(f"[{script}]: Running test case {case}...")

        result = download(idd="YokKp3pwVFc", path="tmp")

        print("Result:")
        pprint(result)
        print(f"[{script}]: Test case {case} complete.")

    else:
        print(f"[{script}]: No test case met.")

    print(f"[{script}]: Testing complete.")
