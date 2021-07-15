## Music Downloader

Download music from Spotify/Youtube Playlist locally using youtube-dll pluggin

## Table of Contents

- [Requirements](#requirements)
- [Features](#features)
- [Usage](#usage)
- [Classes](#classes)
- [Ressources](#ressources)

## [Requirements](#requirements)
## [Features](#features)

Main Features:
- [X] Download Songs from Youtube Playlist
- [ ] Check if songs is already downloaded before downloading it


More:
- [ ] Download Songs from Spotify Playlist
- [ ] Download Books
- [ ] Download Movies

## [Usage](#usage)

#### Step 1: Create virtual environment with venv


`` python3 -m venv music-downloader-venv``
`` source music-downloader-venv/bin/activate ``

Source: [How to create virtual environment in Python](https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/)

#### Step 2: Install Requirements inside venv

`` pip install -r requirements.txt``

#### Step 2.5: Install ffmpeg

On Windows 10: [Download ffmpeg on Windows](https://www.wikihow.com/Install-FFmpeg-on-Windows)
or using chocolatey: ``choco install ffmpeg``

On Ubuntu: ``sudo apt-get install ffmpeg``


#### Optional: Convert Youtube url to mp3 file

`` youtube-dl --extract-audio --audio-format mp3 <video URL> ``

## [Classes](#classes)

- [X] Downloader: download all songs from CSV file if they are not already downloaded
- [X] GeneratorCSV: generate csv file with playlist meta data from youtube music playlist
- [ ] Playlister: from download directory, generate playlist from csv file

## [Ressources](#ressources)

- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [youtube-dl cheatsheet](https://sachithmuhandiram.medium.com/youtube-dl-cheatsheet-bcc0782e7124)
- [tube-dl](https://pypi.org/project/tube-dl)
- [ytmusicapi](https://ytmusicapi.readthedocs.io/en/latest/reference.html#ytmusicapi.YTMusic.get_playlist)


