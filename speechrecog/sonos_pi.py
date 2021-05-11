from soco import SoCo
import youtube_dl
import pafy
import os
from pytube import YouTube

sonos = SoCo('192.168.0.7')
sonos.volume = 20
track = sonos.get_current_track_info()
print(track['title'] + ' by ' + track['artist'])
print(track['uri'])


def test():
    url = 'https://www.youtube.com/watch?v=KbjDreLQs7Y'
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url



    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    v_link = 'https://www.youtube.com/watch?v=KbjDreLQs7Y'

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(v_link, download=False)
        #print(info_dict)
        audio_url = info_dict.get("url", None)
        #print(audio_url)
        sonos.play_uri('flac://' + audio_url)


