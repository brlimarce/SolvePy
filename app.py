'''
** app
| This runs the Flask application.
'''
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import csrf, FlaskForm
from wtforms import FieldList, FormField, RadioField, SubmitField

from templates.layouts import data as d
from api.scripts.forms import QSIForm, ProblemForm, SimplexForm, ComposeForm, Element
from api.scripts import qsi as q
from api.scripts import simplex as s

import sys

app = Flask(__name__, static_folder = 'static') # Redirect the application to this file.
app.config['SECRET_KEY'] = '2d0e13d09775d283668ef17a6f808894' # Generate the secret key in the form.

csrf = csrf.CSRFProtect(app) # Integrate a CSRF token into the app.
Bootstrap(app) # Integrate Bootstrap into the app.

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
    # ** Declaration
    form = QSIForm(request.form) # Store the page's form.
    result = None # Store the result (dictionary)

    # If the form is submitted, collect the data.
    if form.validate_on_submit():
        # Collect vectors of x and y values and the x-value.
        xv = form.xv.data
        yv = form.yv.data
        x = form.x.data

        # Get the clean input and perform QSI.
        clean_data = q.clean_input(xv, yv, x)
        result = q.poly_qsi(clean_data[0], clean_data[1], clean_data[2])

        # Reset the data.
        form.xv.data = form.yv.data = form.x.data = None
    return render_template('qsi.html', pages = d.pages, page = 'qsi', tabs = d.tabs_qsi, form = form, output = result)

# Simplex Generic Solver
@app.route('/solve/simplex', methods = ['GET', 'POST'])
def solve_simplex():
    # ** Declaration
    clen = 0 # Store the number of constraints.
    vlen = 0 # Store the number of variables.

    # Store the page's form.
    compose_form = ComposeForm(request.form)

    # Validate the triggered form.
    if compose_form.validate_on_submit():
        # Store the data into variables.
        clen = int(compose_form.clen.data)
        vlen = int(compose_form.vlen.data)

        # Reset the data.
        compose_form.clen.data = compose_form.vlen.data = None
    
    # Subclass the form and bind a new field.
    class SimplexForm(FlaskForm): pass
    SimplexForm.tableau = FieldList(FormField(Element), min_entries = (clen + vlen + 2) * (clen + 1), max_entries = (clen + vlen + 2) * (clen + 1))
    
    SimplexForm.method = RadioField('method', choices = [('maximization', 'Maximization'), ('minimization', 'Minimization')], default = 'maximization')

    SimplexForm.send = SubmitField('display-simplex')

    # Instantiate the newly created form.
    simplex_form = SimplexForm(request.form)
    if simplex_form.validate_on_submit():
        # Get the data.
        tableau = simplex_form.tableau.data
        print('Tableau:', tableau)
    return render_template('simplex.html', pages = d.pages, page = 'simplex', tabs = d.tabs_simplex, compose_form = compose_form, simplex_form = simplex_form, clen = clen, vlen = vlen)

# Problem-Specific Simplex Solver
@app.route('/solve/simplex/problem', methods = ['GET', 'POST'])
def solve_problem():
    # ** Declaration
    form = ProblemForm(request.form) # Store the page's form.
    result = -1 # Store the result (dictionary)
    tableau = None # Store the initial tableau.
    
    is_display_tableau = False # Determine if the initial tableau is displayed.
    is_get_shipped = False # Determine if the no. of shipped items is displayed.

    # If the form is validated, collect the data.
    if form.validate_on_submit():
        # Collect the input arrays.
        demands = [d.demand.data for d in form.demands]
        supplies = [s.supply.data for s in form.supplies]
        costs = [c.cost.data for c in form.costs]

        # Collect the radio and select choices.
        method = form.method.data
        is_display_tableau = form.is_display_tableau.data
        is_get_shipped = form.is_get_shipped.data

        # Get the clean data and perform Simplex.
        clean_data = s.clean_input(demands, supplies, costs, method)
        tableau = s.create_initial_tableau(clean_data[0], clean_data[1])

        # Get the result from Simplex method.
        result = s.simplex(tableau['tableau'], clean_data[1], bool(is_get_shipped))
    return render_template('problem.html', pages = d.pages, page = 'problem', tabs = d.tabs_problem, plants = d.plants, warehouses = d.warehouses, form = form, tableau = tableau, options = [bool(is_display_tableau), bool(is_get_shipped)], output = result)

# About SolvePy
@app.route('/about')
def about():
    return render_template('about.html', pages = d.pages, page = 'about', tabs = d.tabs_about, information = d.profile)