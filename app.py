'''
** app
| This runs the Flask application.
'''
from flask import Flask, render_template
from templates.layouts import data as d

# Redirect the application to this file.
app = Flask(__name__)

'''
** routes
| This contains the routing for every page.
'''
# Home
@app.route('/')
def index():
    return render_template('index.html')

# QSI Solver
@app.route('/solve/qsi')
def solve_qsi():
    return render_template('qsi.html', pages = d.pages, page = 'q', tabs = d.qsi_tabs)

# Simplex Solver
@app.route('/solve/simplex')
def solve_simplex():
    return render_template('simplex.html', pages = d.pages, page = 's', tabs = d.simplex_tabs, options = d.simplex_options, plants = d.plants, warehouses = d.warehouses)

# About SolvePy
@app.route('/about')
def about():
    return render_template('about.html', pages = d.pages, page = 'a', tabs = d.about_tabs, information = d.about_data)