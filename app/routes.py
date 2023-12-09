from flask import render_template,jsonify
from config import Config
from app import app

from get_data import getCourses , UdemyApiParams

import json
path_cat = './categories.json'




def load_categories():
    with open(path_cat, 'r') as file:
        categories_data = json.load(file)
    return categories_data

@app.context_processor
def inject_categories():
    cats=load_categories()
    return {'cats': cats}



@app.route('/')
@app.route('/home')
def home():
    
    return render_template("home.html", title="Sever reponse")


@app.route('/course')
def course():
    
    
    return render_template("course.html", title="Course")


@app.route("/categories/<cat_name>")
def categories(cat_name):
    
    cat_name = cat_name.replace('-', ' ')
    params = UdemyApiParams(search= cat_name , page_size=2 , is_deals_agreed=True , ratings=4)
    courses = getCourses(params)
    print(courses['results'])
    return render_template("categories.html", title="Categories",cat_name = cat_name,courses = courses)


@app.route("/privacy")
def privacy():
    return render_template("privacy-policy.html", title="Privacy")
