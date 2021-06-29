import requests


class shazamSearchRecommendTool:

    def getSong(self):
        return input('Provide a song for search: ')

    # key for recommend, term for search
    def getResponse(self, qryStrSearch: bool, value):

        headers = {
            'x-rapidapi-key':
            "0f61938f73mshb85735525649975p1c7781jsnf127ced8721d",
            'x-rapidapi-host':
            "shazam.p.rapidapi.com"
            }
        if qryStrSearch is True:
            url = 'https://shazam.p.rapidapi.com/search'
            querystring = {
                "term": value,
                "locale": "en-US",
                "offset": "0",
                "limit": "3"
                }
        else:
            url = 'https://shazam.p.rapidapi.com/songs/list-recommendations'
            querystring = {
                "key": value,
                "locale": "en-US",
            }

        if (requests.get(url, headers=headers, params=querystring)).json():
            return (requests.get(url, headers=headers, params=querystring)).json()
        else:
            return "ERROR ME"

    def getImgLinkDict(self, jsonData: dict):
        imgLinkDict = []
        if jsonData:
            for song in jsonData['tracks']['hits'][:3]:
                imgLinkDict.append(song['track']['title'])
                imgLinkDict.append(song['track']['images']['coverart'])

            iterate = iter(imgLinkDict)
            imgLinkDict = dict(zip(iterate, iterate))
            return imgLinkDict
        else:
            return "ERROR ME!"

    def getDictTopSongs(self, keyValue: int):
        songs = self.getResponse(self, False, keyValue)
        songList = []
        tempList = []
        n = 0
        # print(songs)
        if songs:
            try:
                while n < len(songs['tracks']):
                    for values, keys in songs['tracks'][n].items():
                        if values == 'title':
                            tempList.append(keys)
                        elif values == 'images':
                            tempList.append(keys['coverart'])
                            songList.append(tempList)
                            tempList = []
                    n = n + 1
            except TypeError:
                return "ERROR ME!"
            # print(songList)
            return songList
        else:
            return "ERROR ME!"

    def getTrackKey(self, jsonData: dict):
        trackKeyList = []
        for keys in jsonData['tracks']['hits'][:3]:
            trackKeyList.append(keys['track']['key'])

        return trackKeyList

    def setHitSongs(self, jsonData: dict):
        hitSongList = []
        for song in jsonData['tracks']['hits'][:3]:
            hitSongList.append(song['track']['title'])
        return hitSongList
