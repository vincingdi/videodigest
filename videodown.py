
from pytube import Youtube

def download_video(url):
    yt =  Youtube(url)
    stream = yt.streams.first()
    stream.download()