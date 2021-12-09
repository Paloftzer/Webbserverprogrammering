# __init__.py file

#* This imports the necessary packages to initialize our database.
from flask import Flask #* This imports Flask from the flask library.
from flask_sqlalchemy import SQLAlchemy #* This imports SQLAlchemy which handles our database.
from flask_bcrypt import Bcrypt #* This imports the Bcrypt library which is used to encrypt our passwords.
from flask_login import LoginManager #* This imports the flask login library which is used to allow login.
from market.gen_key import key

#* This creates and initializes our server and database.
app = Flask(__name__) # This initializes our flask application from the library.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db" # This configures our database and gives it a name.
app.config["SECRET_KEY"] = key # This is the key we use to access the database.
db = SQLAlchemy(app) # This initializes our SQLAlchemy instance.
bcrypt = Bcrypt(app) # This initializes our Bcrypt instance.
login_manager = LoginManager(app) # This initializes our LoginManager instance.
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

#* This initializes our routes from our routes.py file.
from market import routes