# routes.py file

#* This imports the necessary packages/modules to route our requests to the correct location and display the correct page.
from flask.helpers import flash # This imports the error message when a user fails to comply with the rules of creating an account.
from flask_login import current_user, login_user, logout_user
from flask_login.utils import login_required # This imports the login function needed to login as well as the logout function needed to logout.
from market import app # This imports our app (website) from our market folder.
from flask import render_template, redirect, request, url_for # This imports only the necessary packages for us to redirect requests to the correct location.
from market.models import Item, User # This imports our Item and User modules from our database model.
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm # This imports our RegisterForm so that we can use it for our routes.
from market import db # This imports our database from the __init__.py file in our market folder.

#* This routes to our main page using the Flask routing system and defines a name for the route.
@app.route("/")
# This defines the first route to always be the home page.
def home():
    # This returns our index.html file from our templates folder.
    return render_template("index.html")

#* This routes to our market page using the flask routing system and defines a name for the route.
@app.route("/market", methods = ["GET", "POST"])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    if request.method == "POST":
        purchased_item = request.form.get("purchased_item")
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations, you have successfully bought {p_item_object.name} for {p_item_object.price}$!", category="success")
            else:
                flash(f"Failed to purchase {p_item_object.name}, you don't have enough money", category="danger")
        return redirect(url_for("market_page"))
    if request.method == "GET":
        # Return all the data from our database and save it as the items variable
        items = Item.query.filter_by(owner=None)
        # This returns our market.html file from our templates folder. It also returns the items variable which holds all the information from our database so that we can display it.
        return render_template("market.html", items=items, purchase_form=purchase_form)

#* This routes to our register page using the Flask routing system and defines a name for the route, as well as using the GET and POST methods to allow communication with our database.
@app.route("/register", methods=["GET", "POST"])
def register_page():
    # This initializes our registerForm, which we use in this route.
    form = RegisterForm()
    if form.validate_on_submit():
        # If the data is valid:
        # We save the data from our form on our register.html page in a variable called user_to_create.
        user_to_create = User(
            username = form.username.data,
            email_address = form.email_address.data,
            password = form.password1.data,
        )
        # This sends the variable to our database.
        db.session.add(user_to_create)
        # This saves the changes to our database.
        db.session.commit()
        # After saving the new user to our database we use the redirect and url_for functions from our flask library to redirect the user to our market.html page.
        return redirect(url_for("market_page"))
    if form.errors != {}:
        # If the data is invalid:
        for err_msg in form.errors.values():
            # This uses the flash function to show the correct error message when an error has occurred.
            flash(f"There was an error creating user: {err_msg}", category="danger")
    # This returns our register.html file from our templates folder. It also communicates that we have used the form variable on this page.
    return render_template("register.html", form=form)

#* This creates a route to the login page
@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        # This creates a variable which gets information from the database
        attempted_user = User.query.filter_by(username = form.username.data).first()
        # If the user and the password match the data stored in the database:
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f"Successfully logged in as {attempted_user.username}", category="success")
            return redirect(url_for("home"))
        else:
            flash("Login failed, please try again!", category="danger")
    return render_template("login.html", form=form)

@app.route("/logout")
def logout_page():
    logout_user()
    flash("Logout successful!", category="info")
    return redirect(url_for("home"))