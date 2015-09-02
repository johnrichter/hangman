from flask import Flask

from models import db
from models.game import Game
from models.user import User
from configuration import DevConfiguration


def create_db(app):
    """
    Initialize the database with our models
    :return: None
    """
    db.create_all(app)


def create_app(config='dev'):
    """
    Create our application and initialize the database.
    :param config: The type of default configuration to load.  [dev, prod]
    :return: An initialized Flask() object
    """
    app = Flask(__name__)

    if config == 'dev':
        app.config.from_object(DevConfiguration)

    db.init_app(app)
    db.create_all(app=app)

    return app
