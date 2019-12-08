#Base code taken from https://github.com/Dr-Crow/cmpt-221-examples/tree/master/Examples/example_of_new_layout
#and then altered to match our needs.
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Optional

# A spot to put most of our Forms
# Contact form
class ContactForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = StringField("Email", validators=[Email(), DataRequired()])
    phone_number = StringField("Phone", validators=[Optional()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")

#Asset form for adding and modifying assets
class AssetForm(FlaskForm):
    uid = StringField('User ID', validators=[DataRequired()],
                        render_kw={"placeholder": "Enter User ID..."})
    asset_name = StringField('Name', validators=[DataRequired()],
                        render_kw={"placeholder": "Enter Asset Name..."})
    model = StringField('Model', validators=[DataRequired()],
                        render_kw={"placeholder": "Enter Asset Model..."})
    status = StringField('Status', validators=[DataRequired()],
                        render_kw={"placeholder": "Enter Asset Status..."})
    deptid = StringField('Department ID', validators=[DataRequired()],
                        render_kw={"placeholder": "Enter Department ID..."})
    submit = SubmitField('Submit')

#Search bar form
class SearchBarForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()],
                        render_kw={"placeholder": "Search by Asset Name..."})
    submit = SubmitField('Search')

