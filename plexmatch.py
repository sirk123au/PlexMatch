PYTHONIOENCODING="UTF-8"  
import fnmatch
import os
from config import ConfigParser
from plexapi.server import PlexServer

config = ConfigParser()
search_folder = config['plex']['search_folder']
baseurl = config['plex']['baseurl']
token = config['plex']['token']

try:
  plex = PlexServer(baseurl, token)
except:
  raise Exception("No Plex server found at: {base_url}".format(base_url=baseurl))

movies = plex.library.section('Movies')
for video in movies.all():
    fname = str(video.locations).strip('[]').split("/")[6]

    for file in os.listdir(search_folder):
        if fnmatch.fnmatch(file, fname):
          #print ("\033[1;32;40m Matched {} ----> {}".format(fname , file))
          match = True
          break
        else:
          match = False
    if not match: print (u"Not Matched {}".format(fname))

