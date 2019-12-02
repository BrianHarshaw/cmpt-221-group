#Base code taken from https://github.com/Dr-Crow/cmpt-221-examples/tree/master/Examples/example_of_new_layout
#and then altered to match our needs.
from flask import render_template, redirect, flash
from sqlalchemy import create_engine

from .. import db
from ..models import User, Asset
from . import main
from .forms import ContactForm, AssetForm
from flask_login import login_user, logout_user, login_required

# Main Index Page
@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('index.html')

# Main Index Page for studentFac
@main.route('/studentFac')
@login_required
def index_sf():
    return render_template('studentFac.html')

#Route that brings a verified user to the add asset form
#Looked up that engines are a good way to add data to a database
@main.route('/addAsset',methods=['GET','POST'])
@login_required
def addAsset():
    form=AssetForm()

    if form.validate_on_submit():
        db_uri = 'sqlite:///db.sqlite'
        engine = create_engine(db_uri)

        ins = Asset.insert().values(
            user_id = form.uid.data,
            asset_name = form.asset_name.data,
            model = form.model.data,
            status = form.status.data,
            department_id = form.deptid.data)

        engAdd = engine.connect()
        engAdd.execute(ins)

        return redirect('/index')

    return render_template('/addAsset.html', form=form)

@main.route('/viewAsset/<asset_id>')
@login_required
def viewAsset():
    asset = Asset.query.filter_by(asset_id=asset_id).first()

    return render_template('/viewAsset.html', 
            asset_id = asset_id,
            asset_name = asset.asset_name,
            asset_model = asset.model,
            asset_status = asset.status,
            asset_deptid = asset.department_id)

@main.route('/modifyAsset/<asset_id>')
@login_required
def modifyAsset():
    asset = Asset.query.filter_by(asset_id=asset_id).first()

    return render_template('/modifyAsset.html')

# redirect root route to login screen
@main.route('/')
def index_login():
    return redirect("/auth/login")

# redirect /login to /auth/login
@main.route("/login")
def form_view():
    return redirect("/auth/login")
