youtube_playlist=https://music.youtube.com/playlist?list=PLzx7xtGqjNzoyuaI8_r39Ore61dm5SNIK
songs_file=songs11.txt
start_num=72
end_num=84

# --- store playlist songs in {songs_file} [ FIXME ]
get_playlist:
	# youtube-dl --skip-download --get-id --get-title -i $(youtube_playlist) >> $(songs_file)
	youtube-dl --skip-download --get-id --get-title --flat-playlist -i -o "url: https://music.youtube.com/watch?v=%(id)s&list=RD%(id)s\ntitle: %(title)s\nauthor: %(author)s\n" $(youtube_playlist) > $(songs_file)


# --- download songs from playlist between index {start_num} and {end_num} if not in archive.txt [ COMPLETED ]
download_items_from_playlist:
	youtube-dl -x --audio-format mp3 --audio-quality 0 --embed-thumbnail --add-metadata --playlist-items $(start_num)-$(end_num) -o "%(uploader)s - %(title)s.%(ext)s" --match-title "^(?!(.* - Topic)).*" --download-archive archive.txt $(youtube_playlist)

# --- download all songs from playlist if not in archive.txt [ COMPLETED ]
download_songs_from_playlist:
	youtube-dl -x --audio-format mp3 --audio-quality 0 --embed-thumbnail --add-metadata -o "%(uploader)s - %(title)s.%(ext)s" --match-title "^(?!(.* - Topic)).*" --download-archive archive.txt $(youtube_playlist)
