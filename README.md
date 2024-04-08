# Recommendify
### Project Aim
 An app to scrape Spotify’s API to allow a user to view their most played songs and artists, view recommendations and create playlists based on recommendations. All with a functional UI based on the following design: <br>
 
<img src="https://github.com/baronwoy/Recommendify/assets/157763277/c0606576-02a2-449e-a663-4461b4111407" width="750" height="314.06">

My Output (Cover Art has yet to be implemented):
<img src="https://github.com/baronwoy/recommendify/assets/157763277/ee281090-caf7-481f-a8d1-00914935af82">


### Built With

[![My Skills](https://skillicons.dev/icons?i=py)](https://skillicons.dev) <br />
Python

* [`tkinter`](https://tkdocs.com/tutorial/index.html) library for the GUI
* [`spotipy`](https://spotipy.readthedocs.io/en/2.22.1/) library for access to the Spotify API
  
## What it does
* Displays a users Top 5 tracks and Top 5 artists of the past 12 months
* Generates 2 series recommendations one based on a users top 5 tracks and one on a users top 5 artists
* Generates a playlist putting together the top 5 tracks and the song recommendations
* Generates a playlist putting together the top 5 artists most popular song and the recommendations
  
## Install
based on the premise that a user would be using a Windows Operating System <br/>

install tkinter
```
pip install tk
```
install spotipy
```
pip install spotipy
```
clone the repository
```
git clone https://github.com/baronwoy/recommendify.git
```
1. Create a Spotify account and log into the [Spotify Developer Dashboard](https://developer.spotify.com). 
2. Create an app from the dashboard and get the `Client ID`, `Client Secret` and enter in a `Redirect Uri`
3. Install pythondotenv
```
pip install python-dotenv
```

4. Create a .env file in the same folder as your python file and enter the details as shown below

```properties
SPOTIPY_CLIENT_ID = PASTE-YOUR-CLIENT-ID-HERE
SPOTIPY_CLIENT_SECRET = PASTE-YOUR-CLIENT-SECRET-HERE
SPOTIPY_REDIRECT_URI = PASTE-YOUR-REDIRECT-URI-HERE
```
5. Once ran it will redirect you to the redirect uri, then just copy and paste the full url of the site you got redirected to inside the console, rerun the program and it will run.
6. it will ask you again to enter in another url when you attempt to generate playlists, do the same as above and the program will run

## Known Issues/Improvments
* No cover art for songs shown yet
* Spotify's API can mess up and not provide an endpoint for Recommendations rendering the app useless
* The recommendation functions can be made into one function called two times
* The layout isn't uniform like the design
* Since the recommendation class recommends songs artists that are present within the top 5 artists can come up as recommended artists
  
