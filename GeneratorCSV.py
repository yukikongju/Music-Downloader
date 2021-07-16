#!/usr/bin/env

""" Class that generate csv file from playlist playlist_id """

import json
import pandas as pd
import requests
import spotipy
from ytmusicapi import YTMusic


class GeneratorCSV:
    def __init__(self, playlist_id, csv_dir):
        """
        playlist_id: playlist of url
        """
        self.playlist_id = playlist_id
        self.csv_dir = csv_dir
        self.playlist_name = self.getYoutubePlaylistName()
        self.df = None  # df is read in main
        #  self.df = self.generateDataFrameFromYoutubeMusicPlaylist()
        #  self.save_df_to_csv()

    def getYoutubePlaylistName(self):
        """ function that return playlist name """
        ytmusic = YTMusic()
        playlist = ytmusic.get_playlist(
            playlistId=self.playlist_id, limit=5)
        return playlist["title"]

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

        # generate dataframe
        COLUMN_NAMES = ['artist', 'title', 'album', 'url', 'isDownloaded']
        df = pd.DataFrame(data, columns=COLUMN_NAMES)
        self.df = df
        return df

    def generateDataFrameFromSpotifyPlaylist(self):
        """ Generate Data Frame of Songs from Spotify Playlist """
        # request playlist information from Spotify API
        #  spotify = spotify.Spotify()
        # generate data
        # generate csv file from data frame
        return 1, 1  # df, playlist_name

    def find_download_url_from_spotify_track(self):
        """docstring for find_download_url_from_spotify_track"""
        pass

    def read_csv_file(self):
        """docstring for read_csv"""
        csv_path = self.csv_dir + self.playlist_name + '.csv'
        print(csv_path)
        self.df = pd.read_csv(csv_path, sep=',')

    def save_df_to_csv(self):  # refractor to csvManager?
        self.df.to_csv(self.csv_dir+self.playlist_name +
                       '.csv', sep=',', index=False)


if __name__ == "__main__":
    #  TO CHANGE
    playlist_id = "PLzx7xtGqjNzoahrq-AQmO7DHbJZtGqZUC"
    generator = GeneratorCSV(playlist_id=playlist_id,
                             csv_dir="Playlist/")
    df = generator.generateDataFrameFromYoutubeMusicPlaylist()
    generator.save_df_to_csv()
