# default values for local test only
# youtube_playlist=https://music.youtube.com/playlist?list=PLzx7xtGqjNzo5-L7RCEZEP9cOLlYBQrH1 # Escapade
# youtube_playlist=https://www.youtube.com/playlist?list=PLzx7xtGqjNzoElKjq_zmpzgoS8RNrqHYh # Sweet
youtube_playlist=https://www.youtube.com/playlist?list=PLzx7xtGqjNzowFXNuirvqG9HEFS3stEWF # Fundraiser
# youtube_playlist=https://www.youtube.com/playlist?list=PLzx7xtGqjNzpigAV-LzHYGqkixgYaZGkT # Quebs
# youtube_playlist=https://www.youtube.com/playlist?list=PLzx7xtGqjNzq2t76-yTBavgi3ITEKZx51 # kpop
#

start_num=2
end_num=57
# songs_file=songs11.txt

#https://music.youtube.com/watch?v=XK_gPPgxkHg&list=RDAMVMnHyZg8uekWM --- download music
# youtube-dl -x --audio-format mp3 --audio-quality 0 --embed-thumbnail --add-metadata -o "%(uploader)s - %(title)s.%(ext)s" --match-title "^(?!(.* - Topic)).*"

# --- store playlist songs in {songs_file} + annotate songs[ FIXME ]
get_playlist:
	youtube-dl --skip-download --get-id --get-title --flat-playlist -i -o "url: https://music.youtube.com/watch?v=%(id)s&list=RD%(id)s\ntitle: %(title)s\nauthor: %(author)s\n" $(youtube_playlist) > $(songs_file) 
	# awk 'NR % 2 == 1 {printf "%d. %s\n", (NR+1)/2, $0} NR % 2 == 0 {print}' $(songs_file) > tmp.txt

# --- download songs from playlist between index {start_num} and {end_num} if not in archive.txt [ COMPLETED ]
download_items_from_playlist:
	youtube-dl -x --audio-format mp3 --audio-quality 0 --embed-thumbnail --add-metadata --playlist-items $(start_num)-$(end_num) -o "%(uploader)s - %(title)s.%(ext)s" --match-title "^(?!(.* - Topic)).*" --download-archive archive.txt $(youtube_playlist)

# --- download all songs from playlist if not in archive.txt [ COMPLETED ]
download_songs_from_playlist:
	youtube-dl -x --audio-format mp3 --audio-quality 0 --embed-thumbnail --add-metadata -o "%(uploader)s - %(title)s.%(ext)s" --match-title "^(?!(.* - Topic)).*" --download-archive archive.txt $(youtube_playlist)

# get video size and download time [ FIXME ]
# youtube-dl -j video_url | gron | grep '^json\.formats\[.\+\]\.filesize = ' | grep -v 'null' | sed 's/^json\.formats\[.*\]\.filesize = //; s/;$/ bytes/' | sort -n

