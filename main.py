import subprocess
from pytubefix import YouTube
from pytubefix.cli import on_progress


def get_link():
    link = subprocess.getoutput("powershell.exe -Command Get-Clipboard")
    return link


link = "https://www.youtube.com/watch?v=44vfe7D6GkQ"


yt = YouTube(link, on_progress_callback = on_progress)

yd = yt.streams.get_highest_resolution()
yd.download("./Downloads")
