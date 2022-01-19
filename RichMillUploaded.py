import spotipy
from spotipy.oauth2 import SpotifyOAuth
from tkinter import *

username = 'Username'
scope = 'user-read-currently-playing'
redir = 'Redirect URL'
client_id="CLIENT_ID"
client_secret="CLIENT_SECRET"
sp_oauth = SpotifyOAuth(client_id=client_id, client_secret= client_secret, redirect_uri=redir, scope=scope)

sp = spotipy.Spotify(auth_manager=sp_oauth)

track = sp.currently_playing()
artist = "No Artist"
trackname = "Nothing Playing"

window = Tk()
window.title("Spotify?")
window.configure(bg='black')

window.geometry("500x200")

tracklabel = Label(window, bg='black', fg = 'medium spring green', text = trackname)
artistlabel = Label(window, bg='black', fg = 'medium spring green', text = artist)
tracklabel.config(font =("Courier", 14))
artistlabel.config(font =("Courier", 13))
tracklabel.place(relx = 0.5, rely = 0.5, anchor = CENTER)
artistlabel.place(relx = 0.5, rely = 0.7, anchor = CENTER)
tracklabel.pack()
artistlabel.pack()

while True:
    track = sp.currently_playing()
    if(track is not None):
        trackname = track['item']['name']
        artist = track['item']['artists'][0]['name']
        tracklabel.config(bg='black', fg = 'spring green', text = trackname)
        tracklabel.place(relx = 0.5, rely = 0.5, anchor=CENTER)
        artistlabel.config(bg='black', fg='spring green', text=artist)
        artistlabel.place(relx=0.5, rely=0.7, anchor=CENTER)
    else:
        trackname = "Nothing Playing"
        artist = "No Artist"
        tracklabel.config(bg='black', fg = 'spring green', text = trackname)
        tracklabel.place(relx = 0.5, rely = 0.5, anchor=CENTER)
        artistlabel.config(bg='black', fg='spring green', text=artist)
        artistlabel.place(relx=0.5, rely=0.7, anchor=CENTER)

    window.update()