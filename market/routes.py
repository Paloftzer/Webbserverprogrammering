'''
This imports the necessary packages/modules to route our requests to the correct location
and display the correct site
'''
from flask.helpers import flash
from market import app
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegisterForm
from market import db

# This routes to our main page.
@app.route("/")
def home():
    return render_template("index.html")

# This routes to our market page.
@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html", name="Phillip", items=items)

# This routes to our register page as well as allows the creation of an account.
#TODO: Allow login
@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username = form.username.data,
            email_address = form.email_address.data,
            password = form.password1.data,
        )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("market_page"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error creating user: {err_msg}", category="danger")
    return render_template("register.html", form=form)