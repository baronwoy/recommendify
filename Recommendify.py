# ~ Import tkinter, spotipy, loadenv and pillow frameworks
from tkinter import *
from tkinter import ttk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from urllib.request import urlopen
from PIL import Image, ImageTk
from playlist import playlistsongs, playlistartists

# ~ gets local environment files for CLIENT ID, CLIENT SECRET and REDIRECT URI
load_dotenv()

# ~ sets the scope of the library to read a users listening history
scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# ~ Sets the main application window
root = Tk()
# ~ Sets the title and base size of the application
root.title("Recommendify")
root.geometry("1280x720")

# ~ Sets the main frame of the application
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# ~ setting frames and borders to keep labels together
topsongs = ttk.Frame(mainframe, padding='3 3 12 12')
topsongs.grid(column=1,row=2)
topsongs['borderwidth'] = 2
topsongs['relief'] = 'raised'
topartist = ttk.Frame(mainframe, padding='3 3 12 12')
topartist.grid(column=6, row=2)
topartist['borderwidth'] = 2
topartist['relief'] = 'raised'


# ~ Labels of text
ttk.Label(mainframe, text='Top 5 Songs of the past 12 months').grid(column=1, row=1, sticky=(W, S))
ttk.Label(mainframe, text='Top 5 Artists of the past 12 months').grid(column=6, row=1, sticky=(W, S))
ttk.Label(mainframe, text='5 Song Recommendations').grid(column=1, row=5, sticky=(W, S))
ttk.Label(mainframe, text='5 Artist Recommendations').grid(column=6, row=5, sticky=(W, S))


# ~ Buttons
ttk.Button(mainframe, text='Generate Playlist on Songs', command=playlistsongs).grid(column=1, row=6, sticky=(W, E))
ttk.Button(mainframe, text='Generate Playlist on Artists', command=playlistartists).grid(column=6, row=6, sticky=(W, E))

# ~ function to get a users top 5 tracks of the past 12 months
def top5tracks():
    # ~ sets the range of data to the past 12 months
    for sp_range in ['long_term']:

        # ~ sets a variable to a dictionary containing information about the users 5 top tracks
        songresults = sp.current_user_top_tracks(time_range=sp_range, limit=5)

        # ~ iterates through the dictionary and shows the name of the song and the artist's name
        for i, item in enumerate(songresults['items']):
            # ~ item['album']['images'][0]['url']) will implement image functionality at a later date
            songname = (str(i + 1) + " "+ item['name'])
            artistname = item['artists'][0]['name']
            ttk.Label(topsongs, text=songname).grid(column=i+1, row=3, sticky=(W))
            ttk.Label(topsongs, text=artistname ).grid(column=i+1, row=4, sticky=(W))
    return songresults

# ~ function to get the top 5 artists of a user
def top5artists():
    # ~ sets the range of data to the past 12 months
    for sp_range in ['long_term']:

        # ~ sets a variable to a dictionary containing information about the users 5 top artists
        artistresults = sp.current_user_top_artists(time_range=sp_range, limit=5)

        # ~ iterates through the dictionary and shows the artist's name
        for i, item in enumerate(artistresults['items']):
            artistname = (str(i+1) + " "+ item['name'])
            ttk.Label(topartist, text=artistname).grid(column=i + 1, row=3, sticky=(S))
    return artistresults


# ~ function to get recommendations based on top 5 tracks of a user
def songrecommendations(songresults):
    # ~ initialise the array of track ids that will be used to seed the recommendations
    trackseed = [" "] * 5

    # ~ iterates through the songresults dictionary and stores each song's unique id
    for i, item in enumerate(songresults['items']):
        trackseed[i] = item['id']

    # ~ sets a variable to a dictionary containing 5 song recommendations based on the 5 songs input
    srecresults = sp.recommendations(seed_tracks=trackseed, limit=5)

    # ~ displays the 5 song recommendations
    for i in range(5):
        recs = srecresults['tracks'][i]['name']
        ttk.Label(mainframe, text=recs).grid(column=i+1, row=6, sticky=(N))
    return srecresults

# ~ function to get artist recommendations based on a users top 5 artists
def artistrecommendations(artistresults):
    # ~ initialise seed array and iterate to store artists unique id
    artistseed = [" "] * 5
    for i, item in enumerate(artistresults['items']):
        artistseed[i] = item['id']

    # ~ sets a variable to a dictionary containing 5 song recommendations based on the 5 artists input
    results = sp.recommendations(seed_artists=artistseed, limit=5)

    # ~ displays the artists of the song recommendations found
    for i in range(5):
        recs = results['tracks'][i]['artists'][0]['name']
        ttk.Label(mainframe, text=recs).grid(column=i + 6, row=6, sticky=(N))
    return results

# ~ function to place the top 5 songs and the recommendations' ids into an array
def collatesongs(songresults, srecresults):
    songids = [" "] * 10
    for i, item in enumerate(songresults['items']):
        songids[i] = item['id']
    for i in range(5, 10):
        songids[i] = srecresults['tracks'][i-5]['id']
    return songids

# ~ function to store and return the most popular song of the top 5 artists of the user
def top5artistsmostpopularsong(artistresults):
    response = [" "] * 5
    for i, item in enumerate(artistresults['items']):
        response[i] = sp.artist_top_tracks(item['id'])
    return response

# ~ function to place the top 5 artists most popular songs and the recommendations' ids into an array
def collateartists(response, results):
    artsongids = [" "] * 10
    for i in range(5):
        artsongids[i] = response[i]['tracks'][0]['id']
    for i in range(5, 10):
        artsongids[i] = results['tracks'][i-5]['id']
    return artsongids

# ~ creates a playlist and adds the top 5 songs and recommendations to a playlist
def playlistsongs(songids):
    user = sp.current_user()
    sp.user_playlist_create(user=user['id'],name='Song Recommendations', description='Recommendation from Recommendify service')
    playlists = sp.user_playlists(user=user['id'])
    pl = playlists['items'][0]
    sp.playlist_add_items(pl['id'], songids)

# ~ creates a playlist and adds the top 5 artists most popular songs and recommendations to a playlist
def playlistartists(artsongids):
    user = sp.current_user()
    sp.user_playlist_create(user=user['id'],name='Artist Song Recommendations', description='Recommendation from Recommendify service')
    playlists = sp.user_playlists(user=user['id'])
    pl = playlists['items'][0]
    sp.playlist_add_items(pl['id'], artsongids)

# ~ run the program
def main():
    sresults = top5tracks()
    aresults = top5artists()
    srecresults = songrecommendations(sresults)
    arecresults = artistrecommendations(aresults)
    songids = collatesongs(sresults, srecresults)
    mostpopsong = top5artistsmostpopularsong(aresults)
    artsongids = collateartists(mostpopsong, arecresults)
    playlistsongs(songids)
    playlistartists(artsongids)
#main()

top5tracks()
top5artists()

# ~ Adds padding to all the widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)
root.mainloop()