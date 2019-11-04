#Base code taken from https://github.com/Dr-Crow/cmpt-221-examples/tree/master/Examples/example_of_new_layout
#and then altered to match our needs.
from flask import Blueprint

# Creates a blueprint for all our code under main
main = Blueprint('main', __name__)

from . import forms, views