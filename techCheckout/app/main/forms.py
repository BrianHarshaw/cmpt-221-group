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
    uid = IntegerField('User ID', validators=[DataRequired(), Length(1, 64)],
                        render_kw={"placeholder": "Enter User ID..."})
    name = StringField('Name', validators=[DataRequired(), Length(1, 64)],
                        render_kw={"placeholder": "Enter Asset Name..."})
    model = StringField('Model', validators=[DataRequired(), Length(1, 64)],
                        render_kw={"placeholder": "Enter Asset Model..."})
    status = StringField('Status', validators=[DataRequired(), Length(1, 64)],
                        render_kw={"placeholder": "Enter Asset Status..."})
    deptid = IntegerField('Department ID', validators=[DataRequired(), Length(1, 64)],
                        render_kw={"placeholder": "Enter Department ID..."})
    submit = SubmitField('Submit')

#Search bar form
class SearchBarForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 64)],
                        render_kw={"placeholder": "Search by Asset Name..."})
    submit = SubmitField('Search')

