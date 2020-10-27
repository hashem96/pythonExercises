# __init__.py
import flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db  = SQLAlchemy()
migrate = Migrate()


app = flask.Flask(__name__) # __name__ is the name of the folder
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)


from . import views, models
