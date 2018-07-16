from datetime import datetime
from app import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    sort = db.Column(db.Integer)

    def __repr__(self):
        return '<Category {}>'.format(self.name)

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(6), index=True, unique=True)
    sort = db.Column(db.Integer)

    def __repr__(self):
        return '<Currency {}>'.format(self.name)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    balance = db.Column(db.Float())
    init_balance = db.Column(db.Float())
    is_active = db.Column(db.Boolean())
    is_ignore_balance = db.Column(db.Boolean())
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    sort = db.Column(db.Integer)

    def __repr__(self):
        return '<Account {}>'.format(self.username)