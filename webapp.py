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
    year = request.args['year']
    return render_template('popular.html')
