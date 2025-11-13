from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bd_fake_pinterest.db"
app.config["SECRET_KEY"] = "RBnW6ALwJGFxaMm95wNXW4181YnE9NOK5u8uIMITGiYzRS4UeazY3C7z2AYIYdZs-S2WBuEvief34BTmqsJ4hWl6BQgpNQtH2ZWy9VEiWPF77uXCr_4"
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = "home"

from pinterest import models

from pinterest import routes