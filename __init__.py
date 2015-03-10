from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import flask_sijax

app = Flask(__name__)
app.config.from_object('config')

oncotypingdb = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

flask_sijax.Sijax(app)

from quadbase import qb_views
from oncotyping import onco_views, onco_models
from indiafightasthma import ifa_views
