#!/usr/bin/env

from Downloader import Downloader
from GeneratorCSV import GeneratorCSV
import os.path
from os import path


def main():
    # Step 1: Identify playlist to download and download directories
    playlist_id = "PLzx7xtGqjNzoElKjq_zmpzgoS8RNrqHYh"
    csv_dir = "Playlist/"
    download_path = "Downloads/"  # "C:/path/to/download"

    # Step 2: Generate CSV file from playlist if it doesn't exist
    # need to check if csv file has already been generated
    generator = GeneratorCSV(playlist_id=playlist_id, csv_dir=csv_dir)
    playlist_name = generator.getYoutubePlaylistName()
    print(playlist_name)
    # check if playlist is in csv dir
    if path.exists(csv_dir+playlist_name+'.csv'):  # read df from csv_path
        print("csv file exists. Reading...")
        # read playlist (optional)
        #  generator.read_csv_file() # TO TEST
    else:
        print("csv file doesn't exists. Creating...")
        generator.generateDataFrameFromYoutubeMusicPlaylist()
        generator.save_df_to_csv()
        print("csv file created in "+csv_dir+playlist_name+'.csv')

    # Step 3: Dowload the songs
    downloader = Downloader(downloadPath=download_path,
                            csv_path=csv_dir+playlist_name+'.csv')
    downloader.download_songs()


if __name__ == "__main__":
    main()
