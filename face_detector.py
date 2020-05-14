import cv2
import numpy as np
import os
import database_manager as database


verbosity = 2

face_cascade = cv2.CascadeClassifier('utils/haarcascade_frontalface_default.xml')



def DetectFace(video_name):
    '''
    Returns face to no face ratio.
    '''

    print("[facedetector]: Detecting faces in '{}'".format(video_name)) if verbosity >= 1 else False

    data = database.load()      # consider making function that only returns part of dict
    video = database.loadVideo(video_name)

    frames_w_faces = 0
    while video.isOpened():
        ret, frame = video.read()

        if ret:     # true if frame was read correctly, false if end is reached
            faces = face_cascade.detectMultiScale(frame, 1.3, 5)

            frames_w_faces += 1 if len(faces) > 0 else 0

            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
                # roi_gray = gray[y:y+h, x:x+w]
                roi = frame[y:y+h, x:x+w]


            if verbosity >= 2:
                cv2.imshow('Frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        else:
            break
        
    video.release()
    cv2.destroyAllWindows()

    ratio = frames_w_faces / data[video_name]['frames']
    ratio = round(ratio, 2)

    return ratio




if __name__ == "__main__":
    print("[facedetector]: Running test...")

    data = database.load()
    
    for d in data:
        print(d)

    result = DetectFace('Circumference of a Circle')
    print('[facedetector]: Result: {}'.format(result))