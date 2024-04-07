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

# ~ Sets the main frame of the application
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# ~ Labels of text
ttk.Label(mainframe, text='Top 5 Songs of the past 12 months').grid(column=1, row=1, sticky=(W, S))
ttk.Label(mainframe, text='Top 5 Artists of the past 12 months').grid(column=2, row=1, sticky=(W, S))
ttk.Label(mainframe, text='5 Song Recommendations').grid(column=1, row=3, sticky=(W, S))
ttk.Label(mainframe, text='5 Artist Recommendations').grid(column=2, row=3, sticky=(W, S))

# ~ Buttons
ttk.Button(mainframe, text='Generate Playlist on Songs').grid(column=1, row=5, sticky=(W, E))
ttk.Button(mainframe, text='Generate Playlist on Artists').grid(column=2, row=5, sticky=(W, E))

# ~ Adds padding to all the widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)
root.mainloop()