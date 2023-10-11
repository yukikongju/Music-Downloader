import requests




def main(playlist_url: str):
    response = requests.get(url=playlist_url)

    response_headers = response.headers
    print(response_headers.keys())

    

if __name__ == "__main__":
    PLAYLIST_URL = "https://music.youtube.com/playlist?list=PLzx7xtGqjNzqro8C2I9znFiNlktJq8cCO"
    main(playlist_url=PLAYLIST_URL)
