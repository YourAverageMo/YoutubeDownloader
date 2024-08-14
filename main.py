import subprocess
from pytube import YouTube


def get_link():
    link = subprocess.getoutput("powershell.exe -Command Get-Clipboard")
    return link


link = "https://www.youtube.com/watch?v=44vfe7D6GkQ"

yt = YouTube(link)

print(yt.title)
