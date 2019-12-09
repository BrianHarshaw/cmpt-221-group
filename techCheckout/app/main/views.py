#Base code taken from https://github.com/Dr-Crow/cmpt-221-examples/tree/master/Examples/example_of_new_layout
#and then altered to match our needs.
from flask import render_template, redirect, flash
from sqlalchemy import create_engine

from .. import db
from ..models import User, Asset
from . import main
from .forms import ContactForm, AssetForm, SearchBarForm
from flask_login import login_user, logout_user, login_required

# Main Index Page
@main.route('/',methods=['GET','POST'])
@main.route('/index',methods=['GET','POST'])
@login_required
def index():
    form=SearchBarForm()

    if form.validate_on_submit():
        asset = Asset.query.filter_by(asset_name=form.name).first()

        if asset != None:
            return redirect("/viewAsset", asset.asset_id)

    return render_template('index.html', sbform=form)

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

#Route to view an asset by inputting the asset id
@main.route('/viewAsset/<asset_id>')
@login_required
def viewAsset():
    asset = Asset.query.filter_by(asset_id=Asset.asset_id).first()

    return render_template('/viewAsset.html', 
            asset_id = asset.asset_id,
            asset_name = asset.asset_name,
            asset_model = asset.model,
            asset_status = asset.status,
            asset_deptid = asset.department_id)

#Route that would be taken to modify an asset, using the id to get to a page where that asset is displayed for modification
@main.route('/modifyAsset/<asset_id>',methods=['GET','POST'])
@login_required
def modifyAsset():
    form=AssetForm()
    asset = Asset.query.filter_by(asset_id=Asset.asset_id).first()

    if form.validate_on_submit():
        asset.asset_name = form.asset_name.data
        asset.model = form.model.data
        asset.status = form.status.data
        asset.department_id = form.department_id.data

        session.commit()

    form.asset_name.data = asset.asset_name
    form.model.data = asset.model
    form.status.data = asset.status
    form.department_id.data = asset.department_id

    return render_template('/modifyAsset.html', form=form)

# redirect root route to login screen
@main.route('/')
def index_login():
    return redirect("/auth/login")

# redirect /login to /auth/login
@main.route("/login")
def form_view():
    return redirect("/auth/login")
