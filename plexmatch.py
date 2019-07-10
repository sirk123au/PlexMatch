PYTHONIOENCODING="UTF-8"  
import fnmatch
import os
import time
from config import ConfigParser
from plexapi.server import PlexServer

config = ConfigParser()
search_folder = config['plex']['search_folder']
baseurl = config['plex']['baseurl']
token = config['plex']['token']
if os.name == 'nt': os.system('cls') 
else: os.system('clear')
try: plex = PlexServer(baseurl, token)
except: raise Exception("No Plex server found at: {base_url}".format(base_url=baseurl))
print(r"Reading Plex Movie List", end='\r', flush=True)
movies = plex.library.section('Movies')
       
for video in movies.all():
    fname = str(video.locations).strip('[]').split("/")[6]
    with open('movies.txt', 'a') as f:
      f.write("%s\n" % fname)
    for file in os.listdir(search_folder):
        if fnmatch.fnmatch(file, fname):
          #print (r"Matched {} ----> {}".format(fname , file), end='\r', flush=True)          
          match = True
          break
        else: match = False
    if not match: print ("Not Matched {}".format(fname))