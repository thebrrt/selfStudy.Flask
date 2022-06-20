# Imports
from datetime import datetime
from flask import Flask, render_template
from . import app

# View/Route Functions
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('about.html')

@app.route('/hello/')
def hello(name=None):
    return render_template(
        'hello_there.html',
        name=name,
        date=datetime.now()
    )

@app.route('/api/data')
def get_data():
    return app.send_static_file('data.json')
