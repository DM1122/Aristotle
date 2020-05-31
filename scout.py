'''
Takes care of searching Youtube according to relevant key terms from database and returns
video info to database.
'''

import os, sys
sys.path.append('./arsite')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arsite.settings')
import django
django.setup()
from library.models import Tag, Video, SearchQuery
from libs import youtubelib
import numpy as np
from pprint import pprint



#region meta
script = os.path.basename(__file__)
verbosity = 3
#endregion


#region globals
query_sample_size = 3
search_sample_size = 3
#endregion


#region functions
def sampleSearchQueries(n):
    '''
    Samples queries to be searched from searchQuery model according to popularity.
    '''
    print(f'[{script}]: Sampling search queries...') if verbosity>=1 else None

    queries = list()
    counts = list()

    for e in SearchQuery.objects.all():
        queries.append(e.query)
        counts.append(e.count)

    if len(queries) == 0:
        print(f'[{script}]: WARNING: SearchQuery is empty.')
        return queries

    counts_total = sum(counts)
    probs = [x/counts_total for x in counts]

    n = len(queries) if n > len(queries) else n

    samples = list(np.random.choice(queries, size=n, replace=False, p=probs))


    print(f'[{script}]: Sampled.') if verbosity>=2 else None
    return samples


def saveVideoData(data):
    Video(
        title=data['title'],
        idd=data['idd'],
        thumbnail=data['thumbnail'],
        author=data['author'],
        published=data['published'],
        description=data['description'],
        duration=data['duration'],
        views=data['views'],
        rating=data['rating'],
        commentCount=data['commentCount']
    ).save()

    print(f'[{script}]: Added "{idd}" to database!') if verbosity>=1 else None


#endregion


if __name__ == '__main__':
    print(f'[{script}]: Running Scout...')

    queries = sampleSearchQueries(n=query_sample_size)

    for query in queries:
        ids = youtubelib.searchYT(query=query, maxResults=search_sample_size)

        for idd in ids:
            data = youtubelib.getYTVideoData(idd=idd)

            saveVideoData(data)



    print(f'[{script}]: Expedition complete.')




