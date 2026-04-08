import subprocess

def download_video(url):
    subprocess.run(["yt-dlp", "-o", "video", "--ffmpeg-location", r"C:\Users\Desktop-PC\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin\ffmpeg.exe", "-S", "ext:mp4:m4a", "--write-auto-subs", "--sub-langs", "en", "--convert-subs", "srt", url])

    
