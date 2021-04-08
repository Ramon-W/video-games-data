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
        highestSalesName = highest_sales(videoGames, year, "title")
        highestSales = highest_sales(videoGames, year, "profit")
        highestScore = highest_score(videoGames, year)
        return render_template('populardata.html', highestSalesName = highestSalesName, highestSales = highestSales, highestScore = highestScore, year = year)
    return render_template('popular.html')

def highest_sales(videoGames, year, version):
    highestSold = videoGames[0]
    highestSoldName = ""
    for game in videoGames:
        if game["Release"]["Year"] == year and game["Metrics"]["Sales"] > highestSold["Metrics"]["Sales"]:
            highestSold = game
    if version == "title":
        return highestSold["Title"]
    else:
        profits = highestSold["Metrics"]["Sales"] * 1000000000
        return profits

    
def highest_score(videoGames, year):
    return "hi"
