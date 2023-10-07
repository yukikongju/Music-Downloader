# youtube_playlist=https://music.youtube.com/playlist?list=PLzx7xtGqjNzo5-L7RCEZEP9cOLlYBQrH1
youtube_playlist=https://music.youtube.com/playlist?list=PLzx7xtGqjNzoyuaI8_r39Ore61dm5SNIK
songs_file=songs11.txt
start_num=116
end_num=131

get_playlist:
	youtube-dl --skip-download --get-id --get-title -i $(youtube_playlist) >> $(songs_file)


download_songs_from_playlist:
	# youtube-dl -x --audio-format mp3 --audio-quality 0 --embed-thumbnail --add-metadata --playlist-start $(start_num) --playlist-end $(end_num) -o "%(uploader)s - %(title)s.%(ext)s" --match-title "^(?!(.* - Topic)).*" --download-archive archive.txt $(youtube_playlist)
	youtube-dl -x --audio-format mp3 --audio-quality 0 --embed-thumbnail --add-metadata -o "%(uploader)s - %(title)s.%(ext)s" --match-title "^(?!(.* - Topic)).*" --download-archive archive.txt $(youtube_playlist)




