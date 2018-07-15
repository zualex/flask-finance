from datetime import datetime
from app import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64), index=True, unique=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Category {}>'.format(self.name)

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(6), index=True, unique=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Currency {}>'.format(self.name)