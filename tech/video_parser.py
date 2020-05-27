import pytube
import json
import os
import database_manager as database


verbosity = 2


def getVideo(url):
    '''
    Given a youtube URL, appends video data to database and downloads video to temp directiory.
    '''
    print('[videoparser]: Getting video from "{}"'.format(url)) if verbosity >= 1 else False

    yt = pytube.YouTube(url)

    stream = downloadYT(yt)

    data = database.load()


    data[yt.title] = {
        'title': yt.title,
        'author': yt.author,
        'description': yt.description,
        'length': yt.length,
        'rating': yt.rating,
        'views': yt.views,
        'thumbnail': yt.thumbnail_url,
        'restriction': yt.age_restricted,
        'abr': stream.abr,
        'acodec': stream.audio_codec,
        'bitrate': stream.bitrate,
        'codecs': stream.codecs,
        'fps': stream.fps,
        'mime': stream.mime_type,
        'res': stream.resolution,
        'vcodec': stream.video_codec,
        'size': stream._filesize,
        'frames': stream.fps*yt.length
    }

    database.dump(data)
    

    print('[videoparser]: Got video successfully') if verbosity >= 1 else False




def downloadYT(yt):
    '''
    Downloads video to tmp directory and returns the stream used.
    '''

    print('[videoparser]: Downloading video') if verbosity >= 2 else False
    stream = yt.streams.filter(progressive=True).first()
    stream.download('tmp')

    return stream



if __name__ == "__main__":
    print("[videoparser]: Running test...")

    getVideo('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    #https://www.youtube.com/watch?v=YokKp3pwVFc
    #https://www.youtube.com/watch?v=dQw4w9WgXcQ
    #https://www.youtube.com/watch?v=WgW_KwtBvro


