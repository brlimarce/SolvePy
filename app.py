'''
** app
| This runs the Flask application.
'''
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import csrf

from templates.layouts import data as d
from api.scripts.forms import QSIForm, ProblemForm, SimplexForm
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
    form = SimplexForm(request.form)

    # If the form is validated, collect the data.
    if form.validate_on_submit():
        print(form.problem.data)
    return render_template('simplex.html', pages = d.pages, page = 'simplex', tabs = d.tabs_simplex, form = form)

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
        clean_data = s.clean_problem_input(demands, supplies, costs, method)
        tableau = s.create_initial_tableau(clean_data[0], clean_data[1])

        # Get the result from Simplex method.
        result = s.simplex(tableau['tableau'], clean_data[1], bool(is_get_shipped))
    return render_template('problem.html', pages = d.pages, page = 'problem', tabs = d.tabs_problem, plants = d.plants, warehouses = d.warehouses, form = form, tableau = tableau, options = [bool(is_display_tableau), bool(is_get_shipped)], output = result)

# About SolvePy
@app.route('/about')
def about():
    return render_template('about.html', pages = d.pages, page = 'about', tabs = d.tabs_about, information = d.profile)