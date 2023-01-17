from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

# initializes the Flask server object
app = Flask(__name__)
app.config.from_object(Config)

# initializes the database object
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# imports the all the routes and models
from app import routes, models
