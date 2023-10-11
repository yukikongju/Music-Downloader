#!/usr/bin/env

""" Class that creates playlist from txt files or other """


class Playlister:
    def __init__(self, playlistName, downloadPath, titles):
        """
        playlistName: Name under which the playlist should be saved
        downloadPath: absolute path of the directory with all the files
        titles: all the songs/books that should be added to the playlist
        """
        self.playlistName = playlistName
        self.downloadPath = downloadPath
        self.titles = titles
