youtube_playlist=https://music.youtube.com/playlist?list=PLzx7xtGqjNzo5-L7RCEZEP9cOLlYBQrH1
songs_file=songs11.txt
start_num=1
end_num=20

download_playlist:
	youtube-dl --skip-download --get-id --get-title -i $(youtube_playlist) >> $(songs_file)

download_songs_from_playlist:
	youtube-dl -x --audio-format mp3 --audio-quality 0 --embed-thumbnail --add-metadata --playlist-start $(start_num) --playlist-end $(end_num) -o "%(uploader)s - %(title)s.%(ext)s" $(youtube_playlist)

