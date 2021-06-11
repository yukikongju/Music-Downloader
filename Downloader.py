#!/usr/bin/env

""" Class which download songs/books not in a repository from a url """


class Downloader:
    def __init__(self, url, downloadPath, titles):
        """
        url: website in where we want to download
        downloadPath: absolute path where files should be downloaded
        titles: list of songs/books to be dowloaded
        """
        self.url = url
        self.downloadPath = downloadPath
        self.titles = titles

    def isInDirectory(self):
        """ Check is song/book is in directory provided (recursive check) """
        pass

    def downloadFromMP3Juice(self):
        """ Download a song not in the directory from MP3Juice"""
        pass

    def downloadFromPDFDrive(self):
        """ Download a book not in the directory from PDFDrive"""
        pass

    def downloadFromZLib(self):
        """ Download a book not in the directory from ZLib"""
        pass
