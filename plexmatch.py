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
library_name = config['plex']['library_name']

if os.name == 'nt': os.system('cls') 
else: os.system('clear')
try: plex = PlexServer(baseurl, token)
except: raise Exception("No Plex server found at: {base_url}".format(base_url=baseurl))

print("Reading Plex Movie List")
movies = plex.library.section(library_name).all()
print("Found {} Movies on Plex".format(len(movies)))
movie_local = os.listdir(search_folder)
print("Found {} in Local Directory".format(len(movie_local)))

for video in movies:
    fname = video.locations[0].strip('[]').split("/")[4]
    for file in movie_local:
        if fnmatch.fnmatch(file, fname):
          print (r"Matched {} ----> {}".format(fname , file))          
          match = True
          break
        else: match = False
    if not match: 
      print ("Not Matched {}".format(fname.replace(':','')))
else:
  print("All Movies Match Plex")