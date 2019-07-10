import sys; sys.getdefaultencoding()
import fnmatch
import os
from config import ConfigParser
from plexapi.server import PlexServer

baseurl = 'http://127.0.0.1:5631'
token = 'gGtsTpapKfADQbe9WaYP'
plex = PlexServer(baseurl, token)

movies = plex.library.section('Movies')
for video in movies.all():
    fname = unicode(str(video.locations).strip('[]').split("/")[6])

    for file in os.listdir('/home/hd15/sirk123au/mnt/gdrive/Media/Movies/'):
        if fnmatch.fnmatch(file, fname):
          #print ("\033[1;32;40m Matched {} ----> {}".format(fname , file))
          match = True
          break
        else:
          match = False
    if not match: print (u"Not Matched {}".format(fname))

