from flask_sqlalchemy import SQLAlchemy

from application import create_app, User, Game


app = create_app()
db = SQLAlchemy(app)

