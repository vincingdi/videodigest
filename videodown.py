import subprocess

def download_video(url):
    subprocess.run(["yt-dlp", "-t", "mp4", url, "-o", "video", "--write-subs", "--convert-subs", "srt", "--ffmpeg-location", r"C:\Users\Desktop-PC\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin\ffmpeg.exe"])

    
