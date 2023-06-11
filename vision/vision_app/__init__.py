from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)

app.app_context().push()

app.config["SECRET_KEY"] = '48391ndquhnf'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///user_information.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

app.config.from_object('config')

from . import views
from . import models
