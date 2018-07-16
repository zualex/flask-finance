import click
from flask import current_app, g
from flask.cli import with_appcontext
from app.models import Currency, Category, Account
from app.seeds.currencies import Currencies
from app.seeds.categories import Categories
from app.seeds.accounts import Accounts
from app import db


def init_app(app):
    app.cli.add_command(seed_command)


@click.command('seed')
@with_appcontext
def seed_command():
    Currency.query.delete()
    click.echo('-----------------')
    click.echo('Remove currencies')
    for data in Currencies.data:
        obj = Currency(**data)
        db.session.add(obj)
        db.session.commit()
        click.echo('Currency ' + obj.symbol + ' created')

    Category.query.delete()
    click.echo('-----------------')
    click.echo('Remove categories')
    for data in Categories.data:
        obj = Category(**data)
        db.session.add(obj)
        db.session.commit()
        click.echo('Category ' + obj.name + ' created')

    Account.query.delete()
    click.echo('---------------')
    click.echo('Remove accounts')
    for data in Accounts.data:
        obj = Account(**data)
        db.session.add(obj)
        db.session.commit()
        click.echo('Account ' + obj.name + ' created')


