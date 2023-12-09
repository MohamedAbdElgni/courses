from flask import render_template,jsonify
from config import Config
from app import app
from app.models import Category , Courses, SubCategory
from get_data import getCourses , UdemyApiParams

import json
path_cat = './categories.json'




def load_categories():
    categories_data = Category.query.all()
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


@app.route("/categories/<slug>")
def categories(slug):
    slug = slug
    selected_cat = SubCategory.query.filter_by(slug=slug).first()
    params = UdemyApiParams(search= slug , page_size=2 , is_deals_agreed=True , ratings=4)
    # courses = getCourses(params)
    # print(courses['results'])
    return render_template("categories.html", title="Categories",selected_cat = selected_cat)


@app.route("/privacy")
def privacy():
    return render_template("privacy-policy.html", title="Privacy")
