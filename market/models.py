# models.py file

#* This imports the needed packages.
from market import db # This imports our database from the market folder.
from market import bcrypt # This imports bcrypt from our market folder so that we can encrypt passwords.

#* This creates a users account as well as their current budget.
#* This defines that a User Table should be added to the database through (db.Model).
class User(db.Model):
    # This creates an integer column for the id in the database, and it is the primary_key.
    id = db.Column(db.Integer(), primary_key=True)
    # This creates a string column for the username in the database, and it can have a max length of 30, cannot be null (empty) and has to be unique.
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    # This creates a string column for the email address in the database, it can have a max length of 50, cannot be null (empty) and has to be unique.
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    # This creates a string column for the password in the database, it can have a max length of 60, and cannot be null (empty).
    password_hash = db.Column(db.String(length=60), nullable=False)
    # This creates an integer column for the budget in the database, it cannot be null (empty), and has a default (starting) value of 1000.
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    item = db.relationship("Item", backref="owned_user", lazy=True)
    @property
    def password(self):
        return self.password
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode("utf-8")

# This generates the items available for purchase as well as their price.
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey("user.id"))