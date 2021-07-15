#!/usr/bin/env

from Downloader import Downloader
from GeneratorCSV import GeneratorCSV


def main():
    # Step 1: Identify playlist to download and download directories
    playlist_id = "RDCLAK5uy_mykviNKPwD0nalgCmKxDkJZ3dhkDl3pSk"
    csv_dir = "Playlist/"
    #  download_path = "C:/Users/emuli/Downloads/"
    download_path = "Downloads/"

    # Step 2: Generate CSV file from playlist
    generator = GeneratorCSV(playlist_id=playlist_id, csv_dir=csv_dir)
    playlist_name = generator.playlist_name

    # Step 3: Check if songs have already been downloaded

    # Step 4: Dowload the songs
    downloader = Downloader(downloadPath=download_path,
                            csv_path=csv_dir+playlist_name+'.csv')
    downloader.download_songs()


if __name__ == "__main__":
    main()
