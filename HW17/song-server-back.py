from flask import Flask, request, render_template
from .shazamClassTool import shazamSearchRecommendTool as shaz

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/data", methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        formData = request.form
        formName = list((formData.to_dict()).values())[0]
        searchResponse = shaz.getResponse(shaz, True, formName)
        keyList = shaz.getTrackKey(shaz, searchResponse)
        similarSongsDict = shaz.getImgLinkDict(shaz, searchResponse)
        if type(similarSongsDict) == str:
            similarSongsDict = {'No Songs --> Song Not Popular Enough.': 'https://image.emojipng.com/158/14092158.jpg'}

        return render_template('data.html', formData=similarSongsDict, keyList=keyList)


@app.route("/recommendations", methods=['GET'])
def recommendations():
    if request.method == 'GET':
        queryStringKey = request.args.get('key')
        songList = shaz.getDictTopSongs(shaz, queryStringKey)
        if type(songList) == str:
            songList = [['No Recommendations --> Song Not Popular Enough.', 'https://image.emojipng.com/158/14092158.jpg']]
        listSize = len(songList)
        return render_template('recommendations.html', recommendData=songList, listSize=listSize)
