.PHONY: 
download_liked_songs: 
	# make headers
	# generate songs.txt
	python3 main.py
	# download using scripts
	./download.sh
	# echo $(PLAYLIST_ID) $(DATEAFTER)


test: 
	youtube-dl --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" playlist_URL


