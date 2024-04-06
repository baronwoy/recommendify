# ~ Import tkinter and spotipy and env libraries
from tkinter import *
from tkinter import ttk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# ~ gets local environment files for CLIENT ID, CLIENT SECRET and REDIRECT URI
load_dotenv()

# ~ Sets the main application window
root = Tk()
# ~ Sets the title and base size of the application
root.title("Recommendify")
root.geometry("1120x469")

# ~ Placeholder to ensure tkinter is working
ttk.Button(root, text="Hello World").grid()
root.mainloop()