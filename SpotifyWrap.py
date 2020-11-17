# encoding=utf8
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_tracks(playlist_id, option=0):
  results = sp.playlist(playlist_id)
  tracks = (r["track"] for r in results["tracks"]["items"])
  formatted_tracks = []
  for track in tracks:
      if not track:
        return None
        break
      if option==1:
          formatted_tracks.append(str(track["name"])+" – " + str(track["artists"][0]["name"]))
      elif option==2:
          formatted_tracks.append(track["name"]+" – " + track["artists"][0]["name"]+ " (" + track["album"]["name"] + ")")
      elif option==3:
          return tracks
          break
      else:
          formatted_tracks.append(track["name"])

          
  return formatted_tracks

def get_popularities(playlist_id):
  results = sp.playlist(playlist_id)
  tracks = (r["track"] for r in results["tracks"]["items"])
  popularities = []
  for track in tracks:
      if not track:
        return None
        break
      popularities.append(track["popularity"])
  return popularities

def get_playlist_name(playlist_id):
  results = sp.playlist(playlist_id)
  return results["name"]

def get_most_popular_songs(tracks, songs=1):
  most_popular = 0
  song_uri = ""
  for t in tracks:
      if t["popularity"] > most_popular:
          most_popular = t["popularity"]
          song_uri = t["uri"]
  return song_uri
    

