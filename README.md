# Music Downloader

Download songs from Youtube Playlist as mp3 files using youtube-dll pluggin

## Prerequisites

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




## Features

Main Features:
- [X] Check if songs is already downloaded before downloading it
- [X] Download Songs from Youtube Playlist
- [ ] Download Songs from Spotify Playlist
- [ ] Copy Playlist from Youtube to Spotify
- [ ] Copy Playlist from Spotify to Youtube
- [X] Created Docker Container using: `sudo docker build -t ubuntu-test:latest .`

More:
- [ ] Download Books
- [ ] Download Movies

## How it Works

1. Choose Youtube Playlist to download and find its Playlist ID
2. Generate CSV file with all download information with ``Downloader.py``
3. Once we generated our csv file, we execute ``GeneratorCSV.py`` to download songs that haven't been downloaded yet

## Usage

Template: In ``main.py``

![image](https://user-images.githubusercontent.com/34996954/125808504-688e06b6-10c9-4b46-a6e1-fae9cb18cdd0.png)
#### Step 0: Download Requirements

#### Step 1: Find youtube playlist to download and identify its playlist id

`` youtube playlist url: https://music.youtube.com/playlist?list=RDCLAK5uy_mykviNKPwD0nalgCmKxDkJZ3dhkDl3pSk``

`` playlist_id = "RDCLAK5uy_mykviNKPwD0nalgCmKxDkJZ3dhkDl3pSk"``

#### Step 2: Specify path where csv file should be downloaded

`` csv_dir = "path/where/csv/should/be/downloaded" ``

#### Step 3: Specify path where songs should be downloaded

`` download_path = "path/where/songs/should/be/downloaded" ``

#### Step 4: Execute the script

`` python main.py``


## Classes

- [X] Downloader: download all songs from CSV file if they are not already downloaded
- [X] GeneratorCSV: generate csv file with playlist meta data from youtube music playlist
- [ ] Playlister: from download directory, generate playlist from csv file

## Ressources

- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [youtube-dl cheatsheet](https://sachithmuhandiram.medium.com/youtube-dl-cheatsheet-bcc0782e7124)
- [tube-dl](https://pypi.org/project/tube-dl)
- [ytmusicapi](https://ytmusicapi.readthedocs.io/en/latest/reference.html#ytmusicapi.YTMusic.get_playlist)
- [ytmusicapi example](https://github.com/sigma67/ytmusicapi/blob/master/tests/test.py)
- [Downloading audio only](https://itsfoss.com/youtube-dl-audio-only/)
- [How to download entire Youtube playlist](https://www.reddit.com/r/software/comments/9lxktm/how_to_download_entire_youtube_playlist/)


