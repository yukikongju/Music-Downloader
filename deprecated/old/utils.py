import youtube_dl
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


def download_like_songs():
    pass


def main():
    #  YTMusic.setup(filepath="headers_auth.json") # edit headers 
    save_songs_url('headers_auth.json', 'songs3.txt', 500)

    

if __name__ == "__main__":
    main()
