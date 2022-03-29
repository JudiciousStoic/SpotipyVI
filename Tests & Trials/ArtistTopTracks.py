import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= 'SPOTIPY_CLIENT_ID',
                                                           client_secret='SPOTIPY_CLIENT_SERVER'))

results = sp.search(q='yeat', limit=50)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])