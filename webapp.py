from flask import Flask, request, Markup, render_template, flash
import os
import json

app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('home.html')

@app.route('/popular')
def render_popular():
    with open('video_games.json') as game_data:
        videoGames = json.load(game_data)
    if 'year' in request.args:
        year = request.args['year']
        popularList = highest_sales(videoGames, year)
        highestScore = highest_score(videoGames, year)
        return render_template('populardata.html', highestSalesName = popularList[0], highestSales = popularList[1], highestSalesNameTwo = popularList[2], 
                               highestSalesTwo = popularList[3], highestSalesNameThree = popularList[4], highestSalesThree = popularList[4], 
                               highestScore = highestScore, year = year)
    return render_template('popular.html')

def highest_sales(videoGames, year):
    popList = []
    highestSold = videoGames[0]
    highestSoldTwo = videoGames[0]
    highestSoldThree = videoGames[0]
    for game in videoGames:
        if game["Release"]["Year"] == int(year):
            if game["Metrics"]["Sales"] > highestSold["Metrics"]["Sales"]:
                highestSold = game
            elif game["Metrics"]["Sales"] > highestSoldTwo["Metrics"]["Sales"]:
                highestSoldTwo = game
            elif game["Metrics"]["Sales"] > highestSoldThree["Metrics"]["Sales"]:
                highestSoldThree = game
    popList.append(highestSold["Title"])
    popList.append(highestSold["Metrics"]["Sales"])
    popList.append(highestSoldTwo["Title"])
    popList.append(highestSoldTwo["Metrics"]["Sales"])
    popList.append(highestSoldThree["Title"])
    popList.append(highestSoldThree["Metrics"]["Sales"])
    return popList
    
def highest_score(videoGames, year):
    return "hi"
