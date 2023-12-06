from flask import render_template
from config import Config
from app import app
import os

@app.route('/')
@app.route('/home')
def home():
    #getting client id and secret from .flaskenv
    return render_template("home.html", title="Sever reponse")


@app.route('/course')
def course():
    
    return render_template("course.html", title="Course")


@app.route("/categories")
def categories():

    return render_template("categories.html", title="Categories")


@app.route("/privacy")
def privacy():
    return render_template("privacy-policy.html", title="Privacy")
