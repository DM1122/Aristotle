"""
Visual awareness. Visual processing.
"""
# stdlib
import os
import random

# project
from components import librarian, visage

script = os.path.basename(__file__)
verbosity = 3


def setup():
    """
    Run component-level setup.
    """
    print(f"[{script}]: Setting up occipital lobe...") if verbosity >= 1 else None

    print(f"[{script}]: Set up complete.") if verbosity >= 2 else None


def parse():
    """TEST parse."""
    idd = "4Uyc7WEdBJY"
    video, file_data = librarian.get_video_file(idd=idd)

    print("frames: ", file_data["frames"])

    face_score = visage.detect_faces(video=video, frames=file_data["frames"])

    model = librarian.get_video_data(idd=idd)

    model.face_score = face_score

    print("SCore: ", face_score)


def update():
    """
    Occipital lobe update.
    """
    print(f"[{script}]: Updating occipital lobe...")

    idds = librarian.get_stored_video_idds()
    random.shuffle(idds)  # TODO: replace by smarter prioritization algo

    for idd in idds:
        if not librarian.get_video_data(idd=idd).parsed_by_visage:
            print(
                f"[{script}]: Idd '{idd}' not yet parsed by visage. Parsing..."
            ) if verbosity >= 1 else None

            video, file_data = librarian.get_video_file(idd=idd)
            face_score = visage.detect_faces(video=video, frames=file_data["frames"])
            model = librarian.get_video_data(idd=idd)
            model.face_score = face_score
            model.parsed_by_visage = True

            print(f"[{script}]: Done.") if verbosity >= 1 else None

    print(f"[{script}]: Update complete.")
