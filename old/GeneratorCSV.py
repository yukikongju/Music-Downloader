#!/usr/bin/env

""" Class that generate csv file from playlist playlist_id """

import json
import pandas as pd
import requests
#  import spotipy
from ytmusicapi import YTMusic


class GeneratorCSV:
    def __init__(self, playlist_id: str, csv_dir: str):
        """
        playlist_id: playlist of url
        """
        self.playlist_id = playlist_id
        self.csv_dir = csv_dir
        self.playlist_name = self.fetchYoutubePlaylistName()
        self.csv_path = f"{self.csv_dir}{self.playlist_name}.csv"
        self.df = None  # df is read in main
        self.track_limit = 2500  # limits of tracks read from playlist

    def fetchYoutubePlaylistName(self) -> list:
        """ function that return playlist name """
        ytmusic = YTMusic()
        playlist = ytmusic.get_playlist(
            playlistId=self.playlist_id, limit=5)
        return playlist["title"]

    def generateCSVFromYoutubeMusicPlaylist(self) -> None:
        """ Generate List of Songs from Youtube Playlist """

        # fetch playlist track from Youtube API
        print(f"Fetching Playlist from Youtube API ...")
        tracksJSON = self.fetchJSONTrackFromYoutubeMusicPlaylistID()

        # Generate all the rows: we want to generate data and then create data frame because it is faster: https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-then-filling-it
        print(f"Generating csv file ...")
        data = []
        for i, track in enumerate(tracksJSON):
            # Get Track information
            artist, title, album, video_id =\
                self.getInformationFromYoutubeMusicTrack(track)
            # append row to dataframe
            if video_id != None:  # sinon, l'url n'est pas valide
                url = self.getVideoURLFromYoutubeVideoID(video_id)
                row = [artist, title, album, url, False]
                data.append(row)

        # generate csv
        self.df = self.createPlaylistDataFrame(data)
        self.save_df_to_csv()
        print(f"Successfully saved csv file in {self.csv_path}!")

    def createPlaylistDataFrame(self, data: list) -> list:
        COLUMN_NAMES = ['artist', 'title', 'album', 'url', 'isDownloaded']
        return pd.DataFrame(data, columns=COLUMN_NAMES)

    def getVideoURLFromYoutubeVideoID(self, video_id: str) -> str:
        return "https://music.youtube.com/watch?v=" + \
            video_id + "list=" + self.playlist_id

    def getInformationFromYoutubeMusicTrack(self, track) -> [str, str, str, str]:
        """ Get Track Info: artist, title, album, video_id """
        artist = track["artists"][0]["name"]
        title = track["title"]
        if track["album"] != None:
            album = track["album"]["name"]
        else:
            album = None
        video_id = track["videoId"]
        return artist, title, album, video_id

    def fetchJSONTrackFromYoutubeMusicPlaylistID(self) -> list:
        """ fetch all track from youtube playlist id
            ref -> https://ytmusicapi.readthedocs.io/en/latest/reference.html
        """
        ytmusic = YTMusic()
        playlist = ytmusic.get_playlist(
            playlistId=self.playlist_id, limit=self.track_limit)
        return playlist["tracks"]

    def updateCSVFileFromYoutubeMusicPlaylist(self) -> None:
        """ Updating csv file with new songs in playlist """
        # Reading csv file as dataframe
        self.read_csv_file()

        # API request for tracks in playlist
        tracksJSON = self.fetchJSONTrackFromYoutubeMusicPlaylistID()

        # create new data to append
        new_data = []
        for index, track in enumerate(tracksJSON):
            # get url of songs
            video_id = track["videoId"]
            if video_id != None:  # sinon, l'url n'est pas valide
                url = self.getVideoURLFromYoutubeVideoID(video_id)
            else:
                continue

            # check if track exists in data frame
            if url not in self.df["url"].values:
                # fetch track information
                artist, title, album, video_id =\
                    self.getInformationFromYoutubeMusicTrack(track)
                row = [artist, title, album, url, False]
                new_data.append(row)
                print("Added: " + artist + " - " + title)

        # update csv file
        newDF = self.createPlaylistDataFrame(new_data)
        frames = [self.df, newDF]
        self.df = pd.concat(frames)  # concat old with new songs
        self.save_df_to_csv()

    def generateDataFrameFromSpotifyPlaylist(self):
        """ Generate Data Frame of Songs from Spotify Playlist """
        pass

    def find_download_url_from_spotify_track(self):
        """docstring for find_download_url_from_spotify_track"""
        pass

    def read_csv_file(self) -> None:
        """docstring for read_csv"""
        csv_path = self.csv_dir + self.playlist_name + '.csv'
        self.df = pd.read_csv(csv_path, sep=',')

    def save_df_to_csv(self) -> None:  # refractor to csvManager?
        self.df.to_csv(self.csv_path, sep=',', index=False)


def main() -> None:
    playlist_id = "PLzx7xtGqjNzoahrq-AQmO7DHbJZtGqZUC"
    generator = GeneratorCSV(playlist_id=playlist_id,
                             csv_dir="Playlist/")
    generator.generateCSVFromYoutubeMusicPlaylist()
    #  df = generator.generateDataFrameFromYoutubeMusicPlaylist()
    #  generator.save_df_to_csv()


if __name__ == "__main__":
    main()
