from flask import Flask, request, url_for, session, redirect
from src.spotify_auth import create_spotify_oauth, get_token, TOKEN_INFO
from src.data_operations import save_json_list_to_csv, get_artist_and_song_names
# from src.download_mp3s import initiate_download
import spotipy


SECRET_KEY = "dslkfj238ru0adfji23"

# App configuration
app = Flask(__name__)

app.secret_key = SECRET_KEY
app.config['SESSION_COOKIE_NAME'] = 'Yash-s Cookie'

# Routes configuration
@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    print(auth_url)
    return redirect(auth_url)

@app.route('/redirect')
def redirectPage():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('getTracks', _external=True))

@app.route('/getTracks')
def getTracks():
    try:
        token_info = get_token()
    except:
        print("user not logged in")
        return redirect(url_for("login", _external=False))
    
    sp = spotipy.Spotify(auth=token_info['access_token'])
    songs_list = []
    iter = 0
    while True:
        items = sp.current_user_saved_tracks(limit=50, offset=iter*50)['items']
        iter+=1
        songs_list += items
        if len(items) < 50:
            break

    csv_file_path = "songs.csv"

    new_list = [song['track'] for song in songs_list]
    save_json_list_to_csv(get_artist_and_song_names(songs_list), csv_file_path)
    # initiate_download()
    return str(len(new_list))
