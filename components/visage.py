"""
Face recognition.

Contrary to facial recognition, visage does not recgonize faces, but detects if faces are present in the frames of a video.
The result is the employment of simpler, more ligthweight algorithms: notably Haar Cascades. Does not make use of Tensorflow.
"""

# stdlib
import os

# external
import cv2

script = os.path.basename(__file__)
verbosity = 3

cascade = cv2.CascadeClassifier("utils/haarcascade_frontalface_default.xml")


def detect_faces(video, frames):
    """
    Detect faces on a per-frame basis. Return a face score.

    Will also release video after use.
    
    Args:
        video (cv2 Video): OpenCV video object
    
    Returns:
        face_score (float): A score from 0-1 that is the ratio of frames with faces to frames w/o
    """
    print(f"[{script}]: Detecting faces in '{video}'...")

    frames_w_faces = 0
    while video.isOpened():
        ret, frame = video.read()

        if ret:  # true if frame was read correctly, false if end is reached
            faces = cascade.detectMultiScale(frame, 1.3, 5)

            frames_w_faces += 1 if len(faces) > 0 else 0

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # roi_gray = gray[y:y+h, x:x+w]
                # roi = frame[y : y + h, x : x + w]

            if verbosity >= 2:
                cv2.imshow("Frame", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

        else:
            break

    video.release()
    cv2.destroyAllWindows()

    face_score = frames_w_faces / frames

    print(f"[{script}]: Face detection complete.")

    return face_score
