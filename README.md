## Useful links

- http://flask.pocoo.org/docs/1.0/
- http://flask-sqlalchemy.pocoo.org/2.3/
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Commands

    $env:FLASK_APP = "finance"
    $env:FLASK_ENV = "development"
    flask run
    flask db init
    flask db migrate -m "tables"
    flask db upgrade
    flask db downgrade
    flask shell

## Custom commands

    flask seed