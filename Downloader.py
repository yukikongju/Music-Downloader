#!/usr/bin/env

""" Class which download songs/books not in a repository from a url """

import youtube_dl
import pandas as pd


class Downloader:
    def __init__(self, downloadPath, csv_path):
        """
        downloadPath: absolute path where files should be downloaded
        df: dataframe of the songs that should be downloaded
        """
        self.downloadPath = downloadPath
        self.csv_path = csv_path
        self.df = self.read_csv_file()
        self.ydl_opts = {
            #  'outtmpl': 'C:/Users/emuli/Downloads/',
            #  'outtmpl': '/tmp/foo_%(title)s-%(id)s.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'keepvideo': False
        }

    def read_csv_file(self):  # refractor in CSVManager?
        """docstring for read_csv_file"""
        df = pd.read_csv(self.csv_path, sep=',')
        return df

    def download_songs(self):
        """ Download songs if it hasn't been downloaded before """
        for index, row in self.df.iterrows():
            if row["isDownloaded"] == False:
                print("Downloading " + row["artist"] + " " + row["title"])
                #  save mp3 as artist+title
                file_name = row["artist"] + '-' + row["title"] + '.mp3'
                self.ydl_opts["outtmpl"] = self.downloadPath + file_name
                with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                    #  download songs
                    song_url = row["url"]
                    ydl.download([song_url])
                    #  set isDownloaded to true
                    #  save updated csv file

    def save_df_to_csv(self):
        pass


if __name__ == "__main__":
    downloader = Downloader(downloadPath="C:/Users/emuli/Downloads/",
                            csv_path="Playlist/playlists.csv")
    downloader.download_songs()
