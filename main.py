import youtube_dl
import subprocess
import os
import pexpect

from ytmusicapi import YTMusic

YOUTUBE_SONG_BASE_URL = "https://music.youtube.com/watch?v="

def get_songs_url_from_liked_videos(headers_file, num_songs):
    """ 
    Get songs url as list from liked video
    """
    ytmusic = YTMusic(headers_file)
    response = ytmusic.get_liked_songs(limit=num_songs)
    tracks = response['tracks']
    songs_urls = []
    for track in tracks:
        videoid = track['videoId']
        url = f"{YOUTUBE_SONG_BASE_URL}{videoid}"
        songs_urls.append(url)
    return songs_urls

def save_songs_url(headers_file, output_file, num_songs = 100):
    urls = get_songs_url_from_liked_videos(headers_file, num_songs)
    with open(output_file, 'w') as f:
        for url in urls:
            f.write(f"{url}\n")


def download_like_songs(download_abs_path: str, songs_path: str):
    """ 
    Download songs in songs_path.txt file as "<author> - <title>"

    """
    # --- read songs from file
    with open(songs_path, 'r') as f:
        song_urls = [ line.strip() for line in f.readlines() ]

    # --- move into download directory
    os.chdir(download_abs_path)

    # --- download songs
    child = pexpect.spawn('/bin/bash')

    for i, url in enumerate(song_urls):
        download_prompt = f"youtube-dl -x --audio-format mp3 --output '%(uploader)s - %(title)s.%(ext)s' {url}"
        print(f"Downloading {i+1}/{len(song_urls)} : {url}")
        child.sendline(download_prompt)
        child.expect(pexpect.EOF)
        output = child.before.decode('utf-8')


def main():
    SONGS_PATH = 'songs/songs5.txt'
    #  YTMusic.setup(filepath="headers_auth.json") # edit headers 
    #  save_songs_url('headers_auth.json', SONGS_PATH, 500)
    download_like_songs('/home/yukikongju/Downloads/', songs_path=SONGS_PATH)

    

if __name__ == "__main__":
    main()
