
from pytube import YouTube

def download_video(url):
    yt =  YouTube(url)
    stream = yt.streams.first()
    stream.download(filename="video")
    caption = yt.captions.get_by_language_code('en')
    str = caption.generate_srt_captions()

    with open("english.srt", "w") as f:
        f.write(str)

    
