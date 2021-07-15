#!/usr/bin/env

""" Class that generate csv file from playlist playlist_id """

import json
import pandas as pd
import requests
from ytmusicapi import YTMusic


class GeneratorCSV:
    def __init__(self, playlist_id):
        """
        playlist_id: playlist of url
        """
        self.playlist_id = playlist_id
        self.df = self.generateDataFrameFromYoutubeMusicPlaylist()

    def generateDataFrameFromYoutubeMusicPlaylist(self):
        """ Generate List of Songs from Youtube Playlist """

        # API request for Youtube Music
        ytmusic = YTMusic()
        playlist = ytmusic.get_playlist(
            playlistId=self.playlist_id, limit=500)
        # json file of tracks: https://ytmusicapi.readthedocs.io/en/latest/reference.html
        tracks = playlist["tracks"]
        #  print(playlist["id"])

        # Generate all the rows: we want to generate data and then create data frame because it is faster: https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-then-filling-it
        data = []
        for i, track in enumerate(tracks):
            # Get Meta Data
            artist = track["artists"][0]["name"]
            title = track["title"]
            if track["album"] != None:
                album = track["album"]["name"]
            else:
                album = None
            #  duration = track["duration"] # TO FIX: duration has bug
            video_id = track["videoId"]
            isDownloaded = False  # TODO: check if song is already downloaded
            # append row to dataframe
            if video_id != None:  # sinon, l'url n'est pas valide
                url = "https://music.youtube.com/watch?v=" + \
                    video_id + "list=" + self.playlist_id
                row = [artist, title, album, url, isDownloaded]
                data.append(row)
            #  df.loc[i] = row  # DONT APPEND DIRECTLY: Too slow

        # generate dataframe
        COLUMN_NAMES = ['artist', 'title', 'album', 'url', 'isDownloaded']
        df = pd.DataFrame(data, columns=COLUMN_NAMES)
        return df

    def generateListFromSpotify(self):
        """ Generate List of Songs from Spotify Playlist """
        pass

    def find_song_url(self):
        """ Find song playlist_id from youtube with key: artist+title+lyrics """
        pass


if __name__ == "__main__":
    playlist_id = "PLzx7xtGqjNzoahrq-AQmO7DHbJZtGqZUC"
    generator = GeneratorCSV(playlist_id)
    #  generator.generateDataFrameFromYoutubeMusicPlaylist()
