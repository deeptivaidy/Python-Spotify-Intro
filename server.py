#!/usr/bin/env python
# -*- coding: utf-8 -*-

#       _                              
#      | |                             
#    __| |_ __ ___  __ _ _ __ ___  ___ 
#   / _` | '__/ _ \/ _` | '_ ` _ \/ __|
#  | (_| | | |  __/ (_| | | | | | \__ \
#   \__,_|_|  \___|\__,_|_| |_| |_|___/ .
#
# A 'Fog Creek'–inspired demo by Kenneth Reitz™


from flask import Flask, request, render_template, jsonify
import os
import spotify_stats
import SpotifyWrap as spotify

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='static', template_folder='template')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

# Dream database. Store dreams in memory for now. 
DREAMS = ['United States Top 50: 85.2/100 for 50 songs']


@app.after_request
def apply_kr_hello(response):
    """Adds some headers to all responses."""
  
    # Made by Kenneth Reitz. 
    if 'MADE_BY' in os.environ:
        response.headers["X-Was-Here"] = os.environ.get('MADE_BY')
    
    # Powered by Flask. 
    response.headers["X-Powered-By"] = os.environ.get('POWERED_BY')
    return response


@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')
    
@app.route('/stats', methods=['GET', 'POST'])
def stats():
    """Simple API endpoint for dreams. 
    In memory, ephemeral, like real dreams.
    """
    # https://open.spotify.com/playlist/4hJ9abkxS8k0zqDHgdizbb
    if request.method == 'POST':
      print(len(request.args))
    # Add a popularity stat to the in-memory database, if given. 
    if 'playlist' in request.args:
        spotify_uri = request.args['playlist']
        #if its not a spotify uri
        if request.args['playlist'][:7] != 'spotify':
            spotify_uri = 'spotify:playlist:' + request.args['playlist'][34:]
        playlist_name = spotify.get_playlist_name(spotify_uri)
        # average_popularity = spotify_stats.average_popularity(request.args['playlist'])
        most_popular_song = spotify_stats.most_popular_song(spotify_uri)
        if playlist_name and most_popular_song:
            playlist_size = len(spotify.get_tracks(spotify_uri))
            DREAMS.append(str(playlist_name)+ ": " +str(most_popular_song) + " for "+ str(playlist_size) + " songs")
            print(spotify_uri)
        else:
            DREAMS.append(request.args['playlist'] + " did not work :( Try again!")
    
    # Return the list of previous values. 
    return jsonify(DREAMS)

if __name__ == '__main__':
    app.run(debug=True)