import click
from flask import current_app, g
from flask.cli import with_appcontext
from app.models import Currency, Category, Account
from app.seeds.currencies import Currencies
from app.seeds.categories import Categories
from app import db


def init_app(app):
    app.cli.add_command(seed_command)


@click.command('seed')
@with_appcontext
def seed_command():
    Currency.query.delete()
    click.echo('Remove currencies')
    for data in Currencies.data:
        obj = Currency(**data)
        db.session.add(obj)
        db.session.commit()
        click.echo('Currency ' + obj.symbol + ' created')

    Category.query.delete()
    click.echo('Remove categories')
    for data in Categories.data:
        obj = Category(**data)
        db.session.add(obj)
        db.session.commit()
        click.echo('Category ' + obj.name + ' created')


