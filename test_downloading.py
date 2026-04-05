
from pytubefix import YouTube
from pytubefix.cli import on_progress


yt = YouTube("https://www.youtube.com/watch?v=2A3LoKK1hAk", on_progress_callback=on_progress)

ys = yt.streams.get_highest_resolution()
ys.download()
caption = yt.captions.get_by_language_code('en')
str = caption.generate_srt_captions()

with open("english.srt", "w") as f:
    f.write(str)

    
