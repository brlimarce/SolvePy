'''
** app
| This runs the Flask application.
'''
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import csrf

from templates.layouts import data as d
from api.scripts.forms import QSIForm, ProblemForm, SimplexForm, Validator
from api.scripts import qsi as q
from api.scripts import simplex as s

app = Flask(__name__, static_folder = 'static') # Redirect the application to this file.
app.config['SECRET_KEY'] = '2d0e13d09775d283668ef17a6f808894' # Generate the secret key in the form.

# Integrate a CSRF token into the app.
csrf = csrf.CSRFProtect(app)

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
    result = -1 # Store the result (dictionary)

    # If the form is submitted, collect the data.
    if form.validate_on_submit():
        # Collect vectors of x and y values and the x-value.
        xv = form.xv.data
        yv = form.yv.data
        x = form.x.data

        # Get the clean input and perform QSI.
        clean_data = q.clean_input(xv, yv, x)
        result = q.poly_qsi(clean_data['xv'], clean_data['yv'], clean_data['x'])

        # Reset the data.
        form.xv.data = form.yv.data = form.x.data = None
    return render_template('qsi.html', pages = d.pages, page = 'qsi', tabs = d.tabs_qsi, form = form, output = result)

# Simplex Generic Solver
@app.route('/solve/simplex', methods = ['GET', 'POST'])
def solve_simplex():
    # ** Declaration
    form = SimplexForm(request.form)
    result = -1 # Store the result
    colnames = None

    # If the form is validated, collect the data.
    if form.validate_on_submit():
        clean_data = s.create_initial_tableau(form.obj_function.data, (form.constraints.data).split('\n'), form.method.data)
        result = s.simplex(clean_data['initial_tableau'], clean_data['is_max'], False)
        colnames = clean_data['colnames']
    return render_template('simplex.html', pages = d.pages, page = 'simplex', tabs = d.tabs_simplex, form = form, colnames = colnames, output = result)

# Problem-Specific Simplex Solver
@app.route('/solve/simplex/problem', methods = ['GET', 'POST'])
def solve_problem():
    # ** Declaration
    form = ProblemForm(request.form) # Store the page's form.
    result = -1 # Store the result
    clean_data = None # Store the initial tableau.

    # If the form is validated, collect the data.
    if form.validate_on_submit():
        # Collect the input arrays.
        demands = [d.demand.data for d in form.demands]
        supplies = [s.supply.data for s in form.supplies]
        costs = [c.cost.data for c in form.costs]

        # Collect the radio and select choices.
        method = form.method.data

        # Create the tableau based on the problem.
        clean_data = s.create_problem_tableau(demands, supplies, costs, method)
        result = s.simplex(clean_data['tableau'], clean_data['is_max'], True)
    return render_template('problem.html', pages = d.pages, page = 'problem', tabs = d.tabs_problem, plants = d.plants, warehouses = d.warehouses, form = form, tableau = clean_data, output = result)

# About SolvePy
@app.route('/about')
def about():
    return render_template('about.html', pages = d.pages, page = 'about', tabs = d.tabs_about, information = d.profile)