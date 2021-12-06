'''
** app
| This runs the Flask application.
'''
import numpy as np

from flask import Flask, render_template, request
from templates.layouts import data as d
from api.scripts.forms import QSIForm
from api.scripts import qsi

app = Flask(__name__) # Redirect the application to this file.
app.config['SECRET_KEY'] = '2d0e13d09775d283668ef17a6f808894' # Generate the secret key in the form.

'''
** routes
| This contains the routing for every page.
'''
# Home
@app.route('/')
def index():
    return render_template('index.html', pages = d.pages)

# QSI Solver
@app.route('/solve/qsi', methods = ['GET', 'POST'])
def solve_qsi():
    # Store the specific form into a variable.
    form = QSIForm(request.form)

    # If the form is submitted, collect the data.
    if form.validate_on_submit():
        # Collect vectors of x and y values and the x-value.
        xv = form.xv.data
        yv = form.yv.data
        x = form.x.data

        # Get the clean input and perform QSI.
        result = qsi.clean_input(xv, yv, x)
    return render_template('qsi.html', pages = d.pages, page = 'qsi', tabs = d.tabs_qsi, form = form)

# Simplex Solver
@app.route('/solve/simplex')
def solve_simplex():
    return render_template('simplex.html', pages = d.pages, page = 'simplex', tabs = d.tabs_simplex, options = d.simplex_options, plants = d.plants, warehouses = d.warehouses)

# About SolvePy
@app.route('/about')
def about():
    return render_template('about.html', pages = d.pages, page = 'about', tabs = d.tabs_about, information = d.profile)