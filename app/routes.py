from flask import render_template
from config import Config
from app import app
import os
import json
path_cat = 'app/categories.json'





@app.route('/')
@app.route('/home')
def home():
    with open(path_cat,'r') as file:
        cat_data = json.load(file)
    print(cat_data[0]['name'])
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
