from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Constant Variable(s)
BASE_URL = " https://www.billboard.com/charts/hot-100/"

# User input
user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Retrieve specified webpage
response = requests.get(f"{BASE_URL}/{user_date}")
html_file = response.text

# Scrape contents for the Top 100 song titles/names of the specified date
soup = BeautifulSoup(html_file, 'html.parser')
all_songs = soup.find_all('h3', id='title-of-a-story', class_='a-no-trucate')
song_names = [song.getText().strip() for song in all_songs]

# Create token.txt file based on Spotify credentials
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        show_dialog=True,
        cache_path="token.txt")
)

user_id = sp.current_user()["id"]

# Search Spotify for the corresponding Top 100 song titles/names
song_uris = []
year = user_date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)

    try:
        uri = result["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"{song} does not exists in Spotify")
    else:
        song_uris.append(uri)

# Create a new private playlist
playlist_name = f"{user_date} Billboard 100"
playlist = sp.user_playlist_create(user_id, playlist_name, public=False)

# Add the song titles/names into the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# To view playlist (https://open.spotify.com/collection/playlists)
playlist = "https://open.spotify.com/collection/playlists"

print("New playlist created.")
print(f"To view, click the URL {playlist}")
