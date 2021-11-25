# -- External Modules
from flask import Flask, render_template

# Redirect the application to this file.
app = Flask(__name__)

# -- Routes
# Below is the routing to other web pages.

# Home
@app.route('/')
def index():
    return render_template('index.html')