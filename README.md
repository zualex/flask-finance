## Useful links

- http://flask.pocoo.org/docs/1.0/
- http://flask-sqlalchemy.pocoo.org/2.3/
- https://habr.com/post/196810/
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Commands

    $env:FLASK_APP = "finance"
    $env:FLASK_ENV = "development"
    flask run
    flask db init
    flask db migrate -m "users table"
    flask db upgrade
    flask db downgrade