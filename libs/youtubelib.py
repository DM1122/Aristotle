from datetime import datetime
from decouple import config
from googleapiclient.discovery import build
import isodate
import os
from pprint import pprint
import pytube


# region meta
script = os.path.basename(__file__)
verbosity = 3
API_KEY = config("API_YOUTUBE_KEY")
# endregion


# region functions
def searchYT(query, maxResults=16):
    """
    Returns list of relevant YT video ids.
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
        maxResults=maxResults,
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


def getYTVideoData(idd):
    """
    Returns dict containing video parameters of interest from given id.
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
    except:
        print(
            f'[{script}]: WARNING: "{idd}" does not have ratings enabled.'
        ) if verbosity >= 2 else None
        data["rating"] = -1

    try:
        data["commentCount"] = response["statistics"]["commentCount"]
    except:
        print(
            f'[{script}]: WARNING: "{idd}" does not have comments enabled.'
        ) if verbosity >= 2 else None
        data["commentCount"] = -1

    print(f"[{script}]: Got video data.") if verbosity >= 2 else None
    return data


def downloadYTVideo(idd, path):
    """
    Downloads video to path and returns the stream data.
    """
    print(f'[{script}]: Downloading YT video "{idd}"...') if verbosity >= 1 else None

    try:
        yt = pytube.YouTube("https://www.youtube.com/watch?v=" + idd)
        stream = yt.streams.filter(progressive=True).first()
        stream.download(path, filename=idd)
    except:
        print(
            f'[{script}]: Failed download of YT video "{idd}".'
        ) if verbosity >= 0 else None
        return None

    data = {
        "id": idd,
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

    print(
        f'[{script}]: Download successful. Saved to "{path}".'
    ) if verbosity >= 2 else None
    return data


# endregion


if __name__ == "__main__":
    print(f"[{script}]: Running tests...")
    case = 0

    if case == 0:
        print(f"[{script}]: Running test case {case}...")

        result = searchYT(query="Never gonna", maxResults=16)

        print("Result:")
        pprint(result)
        print(f"[{script}]: Test case {case} complete.")

    elif case == 1:
        print(f"[{script}]: Running test case {case}...")

        result = getYTVideoData(idd="dQw4w9WgXcQ")

        print("Result:")
        pprint(result)
        print(f"[{script}]: Test case {case} complete.")

    elif case == 2:
        print(f"[{script}]: Running test case {case}...")

        result = downloadYTVideo(idd="YokKp3pwVFc", path="tmp")

        print("Result:")
        pprint(result)
        print(f"[{script}]: Test case {case} complete.")

    else:
        print(f"[{script}]: No test case met.")

    print(f"[{script}]: Testing complete.")
