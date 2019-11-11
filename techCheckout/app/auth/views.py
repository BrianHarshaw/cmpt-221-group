#Base code taken from https://github.com/Dr-Crow/cmpt-221-examples/tree/master/Examples/example_of_new_layout
#and then altered to match our needs.
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm


# Login view for user
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Get login form
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

    # Onces a user submits the form do this
    if form.validate_on_submit():

        # Query the user table by email
        user = User.query.filter_by(email=form.email.data.lower()).first()

        # If user is not empty and password verified
        if user is not None and user.verify_password(form.password.data):
            # Login the user by a built in Flask-Login function
            login_user(user, form.remember_me.data)

            # Next set when user tries to access a page where a login is required. 
            # If next not set, we redirect user to login page
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = '/login'
            return redirect(next)

        # If the email or password incorrect flash a warning
        flash('Invalid email or password.')
        
    return render_template('login.html', form=form)

# Main Index Page
@auth.route('/')
@auth.route('/index')
@login_required
def index():
    return render_template('index.html')

# Logout Notification, return to login page
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect('/login')
