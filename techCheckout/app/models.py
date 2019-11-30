# Base code taken from https://github.com/Dr-Crow/cmpt-221-examples/tree/master/Examples/example_of_new_layout
# and then altered to match our needs.
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager


# Spot for all our models
# Describing the Role Table
class Role(db.Model):
    # Overriding the default name "Role" with roles
    __tablename__ = "role_t"

    # Describing the columns
    role_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    role_name = db.Column(db.Text, nullable=False)

    # Back Reference to User Model
    user_t = db.relationship('User', backref='role', lazy='dynamic')

    # How it should look if we call print
    def __repr__(self):
        return '<Role %r>' % self.role_name


# Describing the User Table
class User(db.Model, UserMixin):
    # Overriding the default name "User" with users
    __tablename__ = "user_t"

    # Describing the columns
    user_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.BigInteger, nullable=True)

    # Foreign Key linking the Role Table
    role_id = db.Column(db.Integer, db.ForeignKey('role_t.role_id'))

    # How it should look if we call print
    def __repr__(self):
        return '<User %r>' % self.first_name

    # Attribute error for passwords
    @property
    def password(self):
        raise AttributeError('password is not a valid attribute')

    # Setter that you use to hash a password
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password);

    # Using werkzeug to verify the password against the hash
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password);

    # Call to return id of a user
    def get_id(self):
        return self.user_id


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
