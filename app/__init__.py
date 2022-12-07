# Base imports
import os

# My modules imports
from config import Config

# Flask imports
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for

# Flask init
app = Flask(__name__)
app.config.from_object(Config)

# DB init
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import *
from app.routes import *
