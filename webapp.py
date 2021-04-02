from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('home.html')
