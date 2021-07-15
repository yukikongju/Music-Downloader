#!/usr/bin/env

""" Class that generate songs/books list from playlist url """

import requests


class Generator:
    def __init__(self, url):
        """
        url: playlist of url
        """
        self.url = url

    def generateListFromYoutubeMusic(self):
        """ Generate List of Songs from Youtube Playlist """
        response = requests.get(self.url)
        if response.status_code == 200:  # successfully reached webpage
            print("Request succesful")
        else:
            print("Request failed")

    def generateListFromSpotify(self):
        """ Generate List of Songs from Spotify Playlist """
        pass

    def generateListFromGoodreads(self):
        """ Generate List of Songs from Youtube Playlist """
        pass


if __name__ == "__main__":
    url = "https://music.youtube.com/playlist?list=PLzx7xtGqjNzoahrq-AQmO7DHbJZtGqZUC"
    generator = Generator(url)
    generator.generateListFromYoutubeMusic()
