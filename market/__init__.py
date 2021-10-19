# This imports the necessary packages to initialize our database.
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# This creates and initializes our database.
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config["SECRET_KEY"] = "123456789123456789123456"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# This imports our routes from our routes.py file.
from market import routes