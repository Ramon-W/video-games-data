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
        scoreList = highest_score(videoGames, year)
        return render_template('populardata.html', highestSalesName = popularList[0], highestSales = popularList[1], highestSalesNameTwo = popularList[2], 
                               highestSalesTwo = popularList[3], highestSalesNameThree = popularList[4], highestSalesThree = popularList[5], 
                               highestScoreName = scoreList[0], highestScore = scoreList[1], highestScoreNameTwo = scoreList[2], 
                               highestScoreTwo = scoreList[3], highestScoreNameThree = scoreList[4], highestScoreThree = scoreList[5], year = year)
    return render_template('popular.html')

@app.route('/explore')
def render_explore():
    with open('video_games.json') as game_data:
        videoGames = json.load(game_data)
    return render_template('explore.html', data=json.dumps(videoGames))

def highest_sales(videoGames, year):
    popList = []
    highestSold = videoGames[3]
    highestSoldTwo = videoGames[3]
    highestSoldThree = videoGames[3]
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
    ratingList = []
    highestRating = videoGames[3]
    highestRatingTwo = videoGames[3]
    highestRatingThree = videoGames[3]
    for game in videoGames:
        if game["Release"]["Year"] == int(year):
            if game["Metrics"]["Review Score"] > highestRating["Metrics"]["Review Score"]:
                highestRating = game
            elif game["Metrics"]["Review Score"] > highestRatingTwo["Metrics"]["Review Score"]:
                highestRatingTwo = game
            elif game["Metrics"]["Review Score"] > highestRatingThree["Metrics"]["Review Score"]:
                highestRatingThree = game
    ratingList.append(highestRating["Title"])
    ratingList.append(highestRating["Metrics"]["Review Score"])
    ratingList.append(highestRatingTwo["Title"])
    ratingList.append(highestRatingTwo["Metrics"]["Review Score"])
    ratingList.append(highestRatingThree["Title"])
    ratingList.append(highestRatingThree["Metrics"]["Review Score"])
    return ratingList
