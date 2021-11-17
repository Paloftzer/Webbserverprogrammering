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
    # This creates a relationship between an item and the user who owns it, the backref keyword is equivalent to adding another relationship() in the Item table. Because of the lazy label it uses lazy loading which means that it only initializes when it is necessary.
    item = db.relationship("Item", backref="owned_user", lazy=True)
    @property
    # This retrieves the password from the password field in the User table.
    def password(self):
        return self.password
    # Initialize the function to set a new password.
    @password.setter
    def password(self, plain_text_password):
        # This takes the plain text password and converts it into a hashed password.
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode("utf-8")

#* This generates the item table.
class Item(db.Model):
    # This creates an integer column for the id in the database, and it is the primary_key.
    id = db.Column(db.Integer(), primary_key=True)
    # This creates a string column for the name of the item in the database, it can have a max length of 30, cannot be null (empty) and has to be unique.
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    # This creates a string column for the barcode in the database, it can have a max length of 12, cannot be null (empty) and has to be unique.
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    # This creates an integer column for the price in the database and it cannot be null (empty).
    price = db.Column(db.Integer(), nullable=False)
    # This creates a string column for the description in the database and it has a max length of 1024 characters, cannot be null (empty).
    description = db.Column(db.String(length=1024), nullable=False)
    # This creates an integer column for the owner of an item. It uses the user id to define who owns it.
    owner = db.Column(db.Integer(), db.ForeignKey("user.id"))