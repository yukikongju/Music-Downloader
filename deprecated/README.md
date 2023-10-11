# Music Downloader


**How to download music from Youtube playlist**

1. Generate `headers_auth.json` file  
    a. Go to selected playlist on 'https://music.youtube.com/' (or liked songs)  
    b. Go to Inspect Tool under `Network > [POST / GET request] > Headers > Request Headers` and put the following keys in a json dictionary:  
	    i. "User-Agent"  
	    ii. "Accept"  
	    iii. "Accept-Language"  
	    iv.  "Content-Type"  
	    v.   "X-Goog-AuthUser"  
	    vi.  "x-origin": "https://music.youtube.com"  
	    vii. "Cookie"  
    c. This header will be used to fetch all the songs url from your playlist  
2. Generate `songs.txt` with links to youtube song url by running `python3 main.py`
3. Run `./download.sh` script to download all songs in `songs.txt` list


## Ressources



