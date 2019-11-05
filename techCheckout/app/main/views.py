#Base code taken from https://github.com/Dr-Crow/cmpt-221-examples/tree/master/Examples/example_of_new_layout
#and then altered to match our needs.
from flask import render_template, redirect, flash
from .. import db
from ..models import User
from . import main
from .forms import ContactForm


# Allows us to declare our views outside the global scope.
# Declare our route to query last names
@main.route('/<last_name>', methods=['GET'])
def last_query(last_name):
    # Query Database for information
    user = User.query.filter_by(last_name=last_name).first()
    if user is None:
        return "<p>The user you looked up can not be found!</p>", 200
    else:
        return "<p>First Name: {first_name} Last Name: {last_name} Email: {email}</p>".format(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email), 200


# redirect root route to login screen
@main.route('/', methods=['GET'])
def index():
    return redirect("/auth/login")


# redirect /login to /auth/login
@main.route("/login")
def form_view():
    return redirect("/auth/login")
