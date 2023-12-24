from bs4 import BeautifulSoup
from requests_html import HTMLSession
from pathlib import Path
import youtube_dl
import requests
import pandas
import os
from pytube import YouTube

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def download_audio2(url, save_path):
    try:
        yt = YouTube(url)
        audio_streams = yt.streams.filter(only_audio=True, file_extension="mp4")
        audio_stream = audio_streams.first()
        audio_stream.download(output_path=save_path)
        print("Audio downloaded successfully!")
    except Exception as e:
        print(e)
        
SAVE_PATH = str(os.path.join(Path.home(), "Downloads/letsFuckingGo"))


def DownloadVideosFromTitles(songs):
	ids = []
	for song in songs[97:98]:
		vid_id = ScrapeVidId(song)
		ids += [vid_id]
	ids = ['https://www.youtube.com/watch?v='+id for id in ids]
	print(f"Downloading {ids}")
	# DownloadVideosFromIds(ids)
	vid_url = ids[0]
	download_audio2(vid_url, SAVE_PATH)
	# download_video_as_mp3(vid_url);

def download_video_as_mp3(video_url):
    # Set options for youtube_dl
    ydl_opts = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': 'mp3',
    'outtmpl': '%(title)s.%(ext)s',
    'verbose': True,  # Add this line for verbose output
    'no_warnings': True,  # Add this line to suppress warnings
}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


def DownloadVideosFromIds(lov):
	SAVE_PATH = str(os.path.join(Path.home(), "Downloads/songs_downloaded_via_the_python_spotify_script"))
	try:
		os.mkdir(SAVE_PATH)
	except:
		print("download folder exists")
	ydl_opts = {
    	'format': 'bestaudio/best',
   		'postprocessors': [{
        		'key': 'FFmpegExtractAudio',
        		'preferredcodec': 'mp3',
        		'preferredquality': '192',
    		}],
		'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(lov)

def ScrapeVidId(query):
	print ("Getting video id for: ", query)
	BASIC="http://www.youtube.com/results?search_query="
	URL = (BASIC + query)
	URL.replace(" ", "+")
	page = requests.get(URL)
	session = HTMLSession()
	response = session.get(URL)
	response.html.render(sleep=1)
	soup = BeautifulSoup(response.html.html, "html.parser")

	results = soup.find('a', id="video-title")
	return results['href'].split('/watch?v=')[1]

def __main__():
	data = pandas.read_csv('../songs.csv')
	print("Found ", len(data), " songs!")
	data['name'] = data['song'] + ' ' +data['artist']
	songs = data['name'].tolist()
	DownloadVideosFromTitles(songs)

__main__()