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
        self.autosave = True  # update csv file every n songs
        self.n = 10  # save file to csv every n songs

    def read_csv_file(self):  # refractor in CSVManager?
        """docstring for read_csv_file"""
        df = pd.read_csv(self.csv_path, sep=',')
        return df

    def download_songs(self):
        """ Download songs if it hasn't been downloaded before """
        # verify if songs have been downloaded

        # download missing songs
        for index, row in self.df.iterrows():
            if row["isDownloaded"] == False:
                print("Downloading " + row["artist"] + " " + row["title"])
                #  save mp3 as artist+title
                file_name = row["artist"] + ' - ' + row["title"] + '.mp3'
                #  self.ydl_opts["outtmpl"] = self.downloadPath + file_name
                self.ydl_opts["outtmpl"] = self.downloadPath + \
                    file_name  # TO CHANGE
                with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                    #  download songs
                    song_url = row["url"]
                    try:
                        ydl.download([song_url])
                        self.df.loc[index, "isDownloaded"] = True
                    except:  # download has failed
                        print(
                            "Download of: " + row["artist"] + " - " + row["title"] + " has failed")
                        self.save_df_to_csv()

            # update csv file every n songs
            if self.autosave and index % self.n == 0:
                print("AUTOSAVING...")
                self.save_df_to_csv()

        #  save updated csv file
        self.save_df_to_csv()

    def save_df_to_csv(self):  # refractor to csv Manager?
        #  new_file_path = self.csv_path.split(".csv")[0] + '_new' + '.csv'
        self.df.to_csv(self.csv_path, sep=',', index=False)


if __name__ == "__main__":
    #  downloader = Downloader(downloadPath="C:/Users/emuli/Downloads/",
    #                          csv_path="Playlist/Emo kid_changes.csv")
    downloader = Downloader(downloadPath="Downloads/",
                            csv_path="Playlist/Emo kid_changes.csv")
    downloader.download_songs()
