import time
from spotipy.oauth2 import SpotifyOAuth
from flask import url_for, session
# from my_secrets import SPOTIFY_CLIENT_SECRET, SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_ID = "cb386a77765d4b2cbb43ad2cd2c41500"
SPOTIFY_CLIENT_SECRET = "1b9c78391fbb436698cef9ef1ce2b6f4"
TOKEN_INFO = "token_info"


def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=url_for('redirectPage', _external=True),
        scope='user-library-read'
    )

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise "Exception"
    
    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60
    if is_expired:
        sp_auth = create_spotify_oauth()
        token_info = sp_auth.refresh_access_token(token_info['refresh_token'])
    return token_info
