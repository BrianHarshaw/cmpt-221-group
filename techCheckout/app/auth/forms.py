# Base code taken from https://github.com/Dr-Crow/cmpt-221-examples/tree/master/Examples/example_of_new_layout
# and then altered to match our needs.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


# login form for login page
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email(), ], render_kw={"placeholder": "Enter Email Address..."})
    password = PasswordField('Password', validators=[DataRequired()],
                             render_kw={"placeholder": "Enter Password..."})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')
