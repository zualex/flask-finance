import os

from flask import Flask



# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'finance.sqlite'),
)


# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from . import database
database.init_app(app)

from .database import db_session
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

from . import transaction
app.register_blueprint(transaction.bp)