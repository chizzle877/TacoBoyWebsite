from flask import current_app as app
from flask import render_template, redirect

@app.route('/')
def root():
    return redirect('/home')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/apply')
def apply_page():
    return render_template('apply.html')

@app.route('/menu')
def menu_page():
    return render_template('menu.html')