"""
Author: Nathaniel Palmer
Task #: Homework 1
Script Task: This script recommends songs back to the user.
             The song recommended is based on user input
"""
import requests


print("Providing the best song recommendations since June 2021")
print("\n")
userSongName = input("Please provide a name of a song: ")


def extractJson(songName: str):

    urlSearch = "https://shazam.p.rapidapi.com/search"
    querystring = {
        "term": songName,
        "locale": "en-US",
        "offset": "0",
        "limit": "3"
        }

    headers = {
        'x-rapidapi-key': "ceb9f636efmsh22f0ef43c426b77p19680ajsn9ab555fe6373",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
        }

    response = requests.get(urlSearch, headers=headers, params=querystring)

    return response.json()


def getSongs(jsonData: dict):
    storeHitSong = []
    # we get len for being dynamic in case of unknown instances
    hitSongAmount = len(jsonData['tracks']['hits'])

    # ensures list stays at 3 in case it is larger than 3
    if hitSongAmount > 3:
        hitSongAmount = 3

    for i in range(hitSongAmount):
        storeHitSong.append(jsonData['tracks']['hits'][i]['track']['title'])
    return storeHitSong


def provideOptionSelection(songList: list, jsonData: dict):
    listLen = len(songList)
    numberSelection = 0

    print("")
    print("Song List")

    # print 3 songs for user to choose from
    for n in range(len(songList)):
        print(str(n + 1) + ":", songList[n])

    while numberSelection > 3 or numberSelection < 1:
        numberSelection = int(
            input(
                "Choose the number (integer) option for song recommendation: "
                )
            )
        if numberSelection > 3 or numberSelection < 1:
            print("Invalid number selection")

    return numberSelection


def getRecommendations(jsonData: dict, numberSelected: int):
    urlRecommend = "https://shazam.p.rapidapi.com/songs/list-recommendations"
    key = jsonData['tracks']['hits'][numberSelected-1]['track']['key']

    querystring = {
        "key": key,
        "locale": "en-US"
        }

    headers = {
        'x-rapidapi-key': "ceb9f636efmsh22f0ef43c426b77p19680ajsn9ab555fe6373",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
        }

    response = requests.get(urlRecommend, headers=headers, params=querystring)

    json20SongList = response.json()

    # prevents error thrown if object/dictionary is empty
    if json20SongList:
        for n in range(20):
            print(str(n+1) + ":", json20SongList['tracks'][n]['title'])
    else:
        print("No Recommendatios for this Song")


# method calls
jsonData = extractJson(userSongName)

topThree = getSongs(jsonData)

songChoice = provideOptionSelection(topThree, jsonData)

getJsonTrack = extractJson(userSongName)

getRecommendations(getJsonTrack, songChoice)
