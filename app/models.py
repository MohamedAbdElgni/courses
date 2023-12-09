from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from datetime import datetime
from . import db


class Category(db.Model):
    id = db.Column(db.String(15), primary_key=True)
    title = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(200), nullable=True)
    url = db.Column(db.String(200), nullable=True)
    image = db.Column(db.String(200), nullable=True)
    types = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    courses = db.relationship('Courses', backref='category', lazy=True)

    # Relationship with subcategories
    subcategories = db.relationship('SubCategory', back_populates='parent_category', lazy=True)

    def __repr__(self):
        return f"Category('{self.title}', '{self.url}', '{self.image}', '{self.created_at}','{self.slug}','{self.id}','{self.courses}')"


class SubCategory(db.Model):
    id = db.Column(db.String(15), primary_key=True)
    title = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(200), nullable=True)
    url = db.Column(db.String(200), nullable=True)
    image = db.Column(db.String(200), nullable=True)
    types = db.Column(db.String(50), nullable=True)
    parent_id = db.Column(db.String(15), db.ForeignKey('category.id'), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    courses = db.relationship('Courses', backref='subcategory', lazy=True, foreign_keys='Courses.subcategory_id')

    # Relationship with parent category
    parent_category = db.relationship('Category', back_populates='subcategories', foreign_keys=[parent_id])

    def __repr__(self):
        return f"SubCategory('{self.title}', '{self.url}', '{self.image}', '{self.created_at}','{self.slug}','{self.types}','{self.parent_id}','{self.id}','{self.courses}')"
    
    
    
class Courses(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(200), nullable=True)
    url = db.Column(db.String(200), nullable=True)
    image = db.Column(db.String(200), nullable=True)
    price = db.Column(db.String(100), nullable=True)
    rating = db.Column(db.String(100), nullable=True)
    instractor  = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    price = db.Column(db.String(100), nullable=True)
    currency = db.Column(db.String(100), nullable=True)
    category_id = db.Column(db.String(15), db.ForeignKey('category.id'), nullable=True)
    subcategory_id = db.Column(db.String(15), db.ForeignKey('sub_category.id'), nullable=True)
    
    def __repr__(self):
        return f"Courses('{self.title}', '{self.url}', '{self.image}', '{self.price}', '{self.rating}', '{self.created_at}','{self.slug}','{self.category_id}','{self.price},'{self.currency}'), '{self.instractor}'"

