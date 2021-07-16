#!/usr/bin/env

from Downloader import Downloader
from GeneratorCSV import GeneratorCSV
import os.path
from os import path


def main():
    # Step 1: Identify playlist to download and download directories
    playlist_id = "RDCLAK5uy_mykviNKPwD0nalgCmKxDkJZ3dhkDl3pSk"
    csv_dir = "Playlist/"
    download_path = "Downloads/"  # "C:/path/to/download"

    # Step 2: Generate CSV file from playlist if it doesn't exist
    generator = GeneratorCSV(playlist_id=playlist_id, csv_dir=csv_dir)
    playlist_name = generator.playlist_name
    # check if playlist is in csv dir
    csv_path = csv_dir+playlist_name+'.csv'
    if path.exists(csv_path):  # Update csv file with new songs
        print(csv_path + " already exists. Updating with new tracks...")
        generator.updateCSVFileFromYoutubeMusicPlaylist()
        print(csv_path + " has been updated.")
    else:
        print(csv_path + " doesn't exists. Creating...")
        generator.generateCSVFromYoutubeMusicPlaylist()
        print("csv file created in " + csv_dir + playlist_name + '.csv')

    # Step 3: Dowload the songs
    downloader = Downloader(downloadPath=download_path,
                            csv_path=csv_dir+playlist_name+'.csv')
    downloader.download_songs()


if __name__ == "__main__":
    main()
