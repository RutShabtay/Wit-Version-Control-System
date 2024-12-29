import click
from wit import Wit
import Exceptions


# !/usr/bin/env python3

@click.group()
def cli():
    pass


@click.command()
def init():
    try:
        Wit.init()
        print("Your project is initialized by Wit.")
    except Exceptions.FileExistsError as e:
        print (e)
    except Exception as e:
        print (e)


cli.add_command(init)


@click.command()
@click.argument('name', type=click.Path())
def add(name):
    try:
        Wit.add(name)
        print ("The file/folder has been successfully added to watchlist by wit.")
    except Exceptions.WitNotExistsError as e:
        print (e)
    except Exceptions.NotValidPathSpec as e:
        print (e)
    except Exceptions.InvalidFileExtension as e:
        print (e)
    except Exception as e:
        print (e.message)


cli.add_command(add)


@click.argument('message', type=click.STRING)
@click.command()
def commit_m_message(message):
    try:
        Wit.commit_m_message(message)
        print ("Your changes have been successfully saved and can be viewed in the commit history.")
    except Exceptions.InvalidCommitId as e:
        print (e)

    except Exception as e:
        print (e.message)


cli.add_command(commit_m_message)


@click.command()
def log():
    try:
        Wit.log()
    except Exception as e:
        print (e.message)


cli.add_command(log)


@click.command()
def status():
    try:
        Wit.status()
    except Exception as e:
        print (e)


cli.add_command(status)


@click.command()
@click.argument('commit_id', type=click.STRING)
def checkout(commit_id):
    try:
        Wit.checkout(commit_id)
        print ("You have returned to the version " + commit_id)
    except Exception as e:
        print (e)


cli.add_command(checkout)

if __name__ == '__main__':
    cli()
