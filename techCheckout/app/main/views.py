#Base code taken from https://github.com/Dr-Crow/cmpt-221-examples/tree/master/Examples/example_of_new_layout
#and then altered to match our needs.
from flask import render_template, redirect, flash
from sqlalchemy import create_engine

from .. import db
from ..models import User, Asset
from . import main
from .forms import ContactForm, AddAsset
from flask_login import login_user, logout_user, login_required


# Allows us to declare our views outside the global scope.
# Declare our route to query last names
@main.route('/<last_name>', methods=['GET'])
@login_required
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

#Route that brings a verified user to the add asset form
#Looked up that engines are a good way to add data to a database
@main.route('/addAsset',methods=['GET','POST'])
@login_required
def addAsset():

    form=AddAsset()
    if form.validate_on_submit():
        db_uri = 'sqlite:///db.sqlite'
        engine = create_engine(db_uri)
        ins = Asset.insert().values(
            user_id=form.UID.data,status=form.status.data,
            model=form.model.data,asset_name=form.asset_name.data,
            department_id=form.DID.data)
        engAdd = engine.connect()
        engAdd.execute(ins)
        return redirect('/index')

    return render_template('/addAsset.html', form=form)

@main.route('/viewAsset')
@login_required
def viewAsset():
    return render_template('/viewAsset.html')

@main.route('/modifyAsset')
@login_required
def modifyAsset():
    return render_template('/modifyAsset.html')

# redirect root route to login screen
@main.route('/')
def index():
    return redirect("/auth/login")


# redirect /login to /auth/login
@main.route("/login")
def form_view():
    return redirect("/auth/login")
