import click
from flask import current_app, g
from flask.cli import with_appcontext
from app.models import Currency, Category, Account
from app import db


def init_app(app):
    app.cli.add_command(seed_command)


@click.command('seed')
@with_appcontext
def seed_command():
    click.echo('Test message')


