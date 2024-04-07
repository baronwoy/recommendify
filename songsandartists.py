import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from playlist import playlistsongs
from playlist import playlistartists

# ~ gets local environment files for CLIENT ID, CLIENT SECRET and REDIRECT URI
load_dotenv()

# ~ sets the scope of the library to read a users listening history
scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# ~ function to get a users top 5 tracks of the past 12 months
def top5tracks():
    # ~ sets the range of data to the past 12 months
    for sp_range in ['long_term']:
        print("Top 5 Songs of the past 12 months")

        # ~ sets a variable to a dictionary containing information about the users 5 top tracks
        songresults = sp.current_user_top_tracks(time_range=sp_range, limit=5)

        # ~ iterates through the dictionary and shows the name of the song and the artist's name
        for i, item in enumerate(songresults['items']):
            print(str(i+1), item['name'], '//', item['artists'][0]['name'])
        print()
    return songresults

# ~ function to get the top 5 artists of a user
def top5artists():
    # ~ sets the range of data to the past 12 months
    for sp_range in ['long_term']:
        print("Top 5 Artists of the past 12 months")

        # ~ sets a variable to a dictionary containing information about the users 5 top artists
        artistresults = sp.current_user_top_artists(time_range=sp_range, limit=5)

        # ~ iterates through the dictionary and shows the artist's name
        for i, item in enumerate(artistresults['items']):
            print(str(i+1), item['name'])
        print()
    return artistresults

# ~ function to get recommendations based on top 5 tracks of a user
def songrecommendations(songresults):
    # ~ initialise the array of track ids that will be used to seed the recommendations
    trackseed = [" "] * 5

    # ~ iterates through the songresults dictionary and stores each song's unique id
    for i, item in enumerate(songresults['items']):
        trackseed[i] = item['id']

    print("5 Song Recommendations")

    # ~ sets a variable to a dictionary containing 5 song recommendations based on the 5 songs input
    srecresults = sp.recommendations(seed_tracks=trackseed, limit=5)

    # ~ displays the 5 song recommendations
    for i in range(5):
        print(srecresults['tracks'][i]['name'])
    print()
    return srecresults

# ~ function to get artist recommendations based on a users top 5 artists
def artistrecommendations(artistresults):
    # ~ initialise seed array and iterate to store artists unique id
    artistseed = [" "] * 5
    for i, item in enumerate(artistresults['items']):
        artistseed[i] = item['id']

    print("5 Artist Recommendations")

    # ~ sets a variable to a dictionary containing 5 song recommendations based on the 5 artists input
    results = sp.recommendations(seed_artists=artistseed, limit=5)

    # ~ displays the artists of the song recommendations found
    for i in range(5):
        print(results['tracks'][i]['artists'][0]['name'])
    print()
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
main()


