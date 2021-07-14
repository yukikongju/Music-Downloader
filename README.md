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

- [ ] Download Songs from Youtube Playlist
- [ ] Download Songs from Spotify Playlist
- [ ] Download Missing Songs from Youtube Playlist
- [ ] Download Songs from text file
- [ ] Duplicate Playlist
- [ ] Download Books
- [ ] Download Movies

## [Usage](#usage)

#### Step 1: Create virtual environment with venv


`` python3 -m venv music-downloader-venv \\
source music-downloader-venv/bin/activate ``

Source: [How to create virtual environment in Python](https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/)

#### Step 2: Install Requirements inside venv

`` pip install -r requirements.txt``

#### Optional: Convert Youtube url to mp3 file

`` youtube-dl --extract-audio --audio-format mp3 <video URL> ``

## [Classes](#classes)

- [ ] Downloader: download all songs from CSV file if they are not already downloaded
- [ ] Playlister: from download directory, generate playlist from csv file
- [ ] Generator:
- [ ] CSVManager:

## [Ressources](#ressources)

- PDF Drive
- MP3Juices.cc
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [youtube-dl cheatsheet](https://sachithmuhandiram.medium.com/youtube-dl-cheatsheet-bcc0782e7124)
- [tube-dl](https://pypi.org/project/tube-dl)


