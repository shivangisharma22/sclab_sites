from flask import Flask

import flask_sijax

app = Flask(__name__)
app.config.from_object('config')

flask_sijax.Sijax(app)

from quadbase import qb_views
from oncotyping import onco_views, onco_admin
from indiafightasthma import ifa_views
