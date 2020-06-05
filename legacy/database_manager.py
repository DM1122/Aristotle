# stdlib
import json
import os

# external
import cv2

## Handler for database & video repository


verbosity = 2
database_path = "data/database.txt"
video_repo_path = "tmp"


def create():
    """
    Creates empty database.
    """
    print(
        '[databasemanager]: Instantiating database at "{}"'.format(database_path)
    ) if verbosity >= 1 else False

    if os.path.isfile(database_path):
        print(
            "[databasemanager]: Warning: database already exists"
        ) if verbosity >= 1 else False
        return

    directory = os.path.split(database_path)[0]
    if not os.path.exists(directory):
        os.mkdir(directory)

    fobj = open(database_path, "w")
    fobj.write("{}")
    fobj.close()

    print(
        "[databasemanager]: Database created successfully"
    ) if verbosity >= 2 else False


def load():
    """
    Returns opened database json data.
    """
    print("[databasemanager]: Loading database") if verbosity >= 1 else False

    try:
        fobj = open(database_path, "r")
    except:
        raise Exception("[databasemanager]: Database file could not be opened")

    data = json.load(fobj)
    fobj.close()

    return data


def clear():
    """
    Clears database.
    """
    print("[databasemanager]: Clearing database") if verbosity >= 1 else False

    try:
        fobj = open(database_path, "r+")
    except:
        raise Exception("[databasemanager]: Database file could not be opened")

    fobj.truncate(0)
    fobj.write("{}")
    fobj.close()


def dump(data):
    print("[databasemanager]: Dumping data to database") if verbosity >= 2 else False

    try:
        fobj = open(database_path, "w")
    except:
        raise Exception("[databasemanager]: Database file could not be opened")

    json.dump(data, fobj, indent=4)


def loadVideo(name):
    """
    Returns the specfied video object from video repository.
    Remeber to free video after use by calling release().
    """
    print(
        '[databasemanager]: Loading video "{}..."'.format(name[0:16])
    ) if verbosity >= 1 else False

    video_path = (
        video_repo_path + "/" + name + ".mp4"
    )  # will not work with all filetypes

    if not os.path.isfile(video_path):
        raise Exception(
            "[databasemanager]: Video could not be found in repository. Consider"
            " downloading it first."
        )

    video = cv2.VideoCapture(video_path)

    if not video.isOpened:
        raise Exception("[facedetector]: Video file could not be opened")

    return video


if __name__ == "__main__":
    print("[databasemanager]: Running test...")

    create()
    input("Press any key to reset...")
    clear()
