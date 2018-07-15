import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

# from app.models import User
from app import db

bp = Blueprint('transaction', __name__, url_prefix='/')


@bp.route('/')
def index():
    # u = User(username='susan2', email='susan2@example.com')
    # db.session.add(u)
    # db.session.commit()

    # data = User.query.first().username
    # data = User.query.first().email
    data = '123'
    return render_template('transaction/index.html', data=data)