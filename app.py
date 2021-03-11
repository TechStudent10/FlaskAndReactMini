# IMPORTS
from flask import Flask, render_template, url_for
from api import api

# INITIALIZATION
app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")

# PATH FUNCTION
def path(rule, function, **options):
    app.add_url_rule(rule, function.__name__, function, **options) 

# REACT TEMPLATE
def react(**kwargs):
    return render_template('index.html', **kwargs)

# VIEWS
def index():
    return react()

def about():
    return react()

# ADD VIEWS
path('/', index)
path('/about', about)

# RUN FLASK
if __name__ == "__main__":
    app.run(debug=True)