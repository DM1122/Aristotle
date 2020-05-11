import pytube
import json
import os


verbosity = 2


def getVideo(url):
    '''
    Given a youtube URL, appends video data to database and downloads video to temp directiory.
    '''

    print('[videoparser]: Getting video from "{}"'.format(url)) if verbosity >= 1 else False
    yt = pytube.YouTube(url)
    printYT(yt) if verbosity >= 3 else False
    downloadYT(yt)

    if not os.path.isfile('database.txt'):
        open('database.txt', 'a').close()


    with open('database.txt', 'r') as fobj:
        print('[videoparser]: Loading database') if verbosity >= 2 else False
        try:
            data = json.load(fobj)
        except:
            print('[videoparser]: Database is empty. Instantiating database') if verbosity >= 2 else False
            data = {}


    data[yt.title] = {
        'Author': yt.author,
        'Description': yt.description,
        'Length': yt.length,
        'Rating': yt.rating,
        'Views': yt.views,
        'Thumbnail': yt.thumbnail_url,
        'Restriction': yt.age_restricted
    }

    
    with open('database.txt', 'w') as fobj:
        print('[videoparser]: Dumping data to database') if verbosity >= 2 else False
        json.dump(data, fobj, indent=4)
    
    print('[videoparser]: Got video successfully') if verbosity >= 1 else False


def printYT(yt):
    '''
    Prints youtube video object to console.
    '''

    print('--Youtube Video Object--')
    print('Title: {}'.format(yt.title))
    print('Author: {}'.format(yt.author))
    print('Description: {}'.format(yt.description[0:32]))
    print('Length (s): {}'.format(yt.length))
    print('Rating (/5): {}'.format(yt.rating))
    print('Views: {}'.format(yt.views))
    print('Thumbnail: {}'.format(yt.thumbnail_url))
    print('Restriction: {}'.format(yt.age_restricted))


def downloadYT(yt):
    print('[videoparser]: Downloading video') if verbosity >= 2 else False
    stream = yt.streams.filter(progressive=True).first()
    stream.download('tmp')



if __name__ == "__main__":
    print("[videoparser]: Running test...")

    getVideo('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


