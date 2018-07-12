import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

from .database import db_session
from .models import User

bp = Blueprint('transaction', __name__, url_prefix='/')


@bp.route('/')
def index():
    # u = User('admin2', 'admin2@localhost')
    # db_session.add(u)
    # db_session.commit()

    # data = User.query.first().name
    # data = User.query.first().email
    data = '123'
    return render_template('transaction/index.html', data=data)