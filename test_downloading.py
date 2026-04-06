


import subprocess

def download_video(url):
    subprocess.run(["yt-dlp", url, ])
    
download_video("https://www.youtube.com/watch?v=jNQXAC9IVRw")
