from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('home.html')

@app.route('/popular')
def render_popular():
    with open('video_games.json') as video_game:
        game = json.load(video_game)
