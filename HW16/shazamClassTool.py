"""
Author: Nathaniel Palmer
Task #: Homework 2
Script Task: This script recommends songs back to the user.
             The song recommended is based on user input
"""
import requests


class shazamSearchRecommendTool:

    def __init__(self):
        self.urlSearch = 'https://shazam.p.rapidapi.com/search'
        self.urlRe = 'https://shazam.p.rapidapi.com/songs/list-recommendations'

    def getSong(self):
        return input('Provide a song for search: ')

    def getResponse(self, url, key, value):

        headers = {
            'x-rapidapi-key':
            "ceb9f636efmsh22f0ef43c426b77p19680ajsn9ab555fe6373",
            'x-rapidapi-host':
            "shazam.p.rapidapi.com"
            }

        querystring = {
            key: value,
            "locale": "en-US",
            # "offset": "0",
            # "limit": "3"
            }

        return requests.get(url, headers=headers, params=querystring)

    def setHitSongs(self, jsonData: dict):
        hitSongList = []
        for song in jsonData['tracks']['hits'][:3]:
            hitSongList.append(song['track']['title'])
        return hitSongList

    def songNumbrSelection(self, hitSongList):
        numberSelection = 0

        print("")
        print("Song List")

        # print 3 songs for user to choose from
        for n in range(len(hitSongList)):
            print(str(n + 1) + ":", hitSongList[n])

        while numberSelection > 3 or numberSelection < 1:
            numberSelection = int(
                input(
                    "Select a (int) option for a song recommendation: "
                    )
                )
            if 1 > numberSelection > 3:
                print("Invalid number selection")

        return numberSelection

    def printRecommendations(self, jsonData: dict, numberSelected: int):
        keyValue = jsonData['tracks']['hits'][numberSelected-1]['track']['key']

        recommendationResponse = self.getResponse(self.urlRe, "key", keyValue)

        recommendationSongJson = recommendationResponse.json()
        # prevents error thrown if object/dictionary is empty
        if recommendationSongJson:
            for n in range(20):
                print(
                    str(n+1) + ":",
                    recommendationSongJson['tracks'][n]['title']
                    )
        else:
            print("No Recommendatios for this Song")

    def userInterface(self):
        songSelected = self.getSong()
        searchResponse = self.getResponse(self.urlSearch, "term", songSelected)
        numberSelected = self.songNumbrSelection(
            self.setHitSongs(searchResponse.json())
            )
        self.printRecommendations(searchResponse.json(), numberSelected)


shizzy = shazamSearchRecommendTool()

shizzy.userInterface()
