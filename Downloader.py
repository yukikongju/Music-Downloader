#!/usr/bin/env

""" Class which download songs/books not in a repository from a url """

import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Downloader:
    def __init__(self, downloadPath, titles):
        """
        url: website in where we want to download
        downloadPath: absolute path where files should be downloaded
        titles: list of songs/books to be dowloaded
        """
        #  self.url = url
        self.downloadPath = downloadPath
        self.titles = titles

    def isInDirectory(self, title):
        """ Check is song/book is in directory provided (recursive check) """
        pass

    def downloadFromMP3Juice(self):
        """ Download a song not in the directory from MP3Juice"""
        # initializing chrome as web browser
        url = "https://www.mp3juices.cc/"
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)  # opening the website

        # Download all songs not in download directory
        for title in self.titles:
            if not isInDirectory(title):
                # Download the first entry
                download_button = driver.find_element_by_name('download')
                download_button.click()

    def downloadFromPDFDrive(self):
        """ Download a book not in the directory from PDFDrive"""
        pass

    def downloadFromZLib(self):
        """ Download a book not in the directory from ZLib"""
        pass


if __name__ == "__main__":
    downloader = Downloader("C:/Downloads", ['mgk'])
    downloader.downloadFromMP3Juice()
