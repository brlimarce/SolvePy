'''
** app
| This runs the Flask application.
'''
from flask import Flask, render_template

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
    return render_template('qsi.html')

# Simplex Solver
@app.route('/solve/simplex')
def solve_simplex():
    return render_template('simplex.html')

# About SolvePy
@app.route('/about')
def about():
    return render_template('about.html')