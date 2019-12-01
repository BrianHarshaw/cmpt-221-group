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


class AddAsset(FlaskForm):
    UID = StringField("User ID", validators=[DataRequired()])
    status = StringField("Status", validators=[DataRequired()])
    model = StringField("Model", validators=[DataRequired()])
    asset_name = StringField("Asset Name", validators=[DataRequired()])
    DID = StringField("Department ID", validators=[DataRequired()])
    submit = SubmitField("Submit")