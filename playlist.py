# ~ Import spotipy and env libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# ~ gets local environment files for CLIENT ID, CLIENT SECRET and REDIRECT URI
load_dotenv()

# ~ sets the scope of the library to modify a users public playlists
scope = 'playlist-modify-public'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# ~ creates a playlist and adds the top 5 songs and recommendations to a playlist
def playlistsongs(songids):
    user = sp.current_user()
    sp.user_playlist_create(user=user['id'],name='Song Recommendations', description='Recommendation from Recommendify service')
    playlists = sp.user_playlists(user=user['id'])
    pl = playlists['items'][0]
    print(pl['id'], pl['name'])
    sp.playlist_add_items(pl['id'], songids)

# ~ creates a playlist and adds the top 5 artists most popular songs and recommendations to a playlist
def playlistartists(artsongids):
    user = sp.current_user()
    sp.user_playlist_create(user=user['id'],name='Artist Song Recommendations', description='Recommendation from Recommendify service')
    playlists = sp.user_playlists(user=user['id'])
    pl = playlists['items'][0]
    print(pl['id'], pl['name'])
    sp.playlist_add_items(pl['id'], artsongids)