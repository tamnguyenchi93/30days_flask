from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nctam1'}
    return render_template('index.html', title='Home page', user=user);