# encoding=utf8
import SpotifyWrap as spotify
# [10, 20, 40, 60, 20]
#Finds our average popularity rating for the tracks in a given spotify playlist
#spotify:playlist:4hJ9abkxS8k0zqDHgdizbb
def average_popularity(playlist="spotify:playlist:37i9dQZEVXbLRQDuF5jeBp"):
    track_popularities = spotify.get_popularities(playlist)
    if track_popularities:
        sum = 0.0
        for pop in track_popularities:
            sum = sum + pop
        num_tracks = len(track_popularities)
        average = sum/num_tracks
        return average
    else:
        return None
      
# encoding=utf8
def most_popular_song(playlist):
    tracks = spotify.get_tracks(playlist, 1)
    track_popularities = spotify.get_popularities(playlist)
    most_popular_index = 0
    most_popular_value = 0
    for index in range(len(track_popularities)):
        if most_popular_value < track_popularities[index]:
            most_popular_index = index
            most_popular_value = track_popularities[index]
    return tracks[index]
            
