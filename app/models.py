from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from . import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(200), nullable=True)
    url = db.Column(db.String(200), nullable=True)
    image = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    courses = db.relationship('Courses', backref='category', lazy=True)
    def __repr__(self):
        return f"Category('{self.title}', '{self.url}', '{self.image}', '{self.created_at}')"

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(200), nullable=True)
    url = db.Column(db.String(200), nullable=True)
    image = db.Column(db.String(200), nullable=True)
    price = db.Column(db.String(100), nullable=True)
    rating = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    def __repr__(self):
        return f"Courses('{self.title}', '{self.url}', '{self.image}', '{self.price}', '{self.rating}', '{self.created_at}','{self.slug}','{self.category_id}')"

