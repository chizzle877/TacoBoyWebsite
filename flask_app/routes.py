import os
from flask import current_app as app, flash, request, url_for
from flask import render_template, redirect
from flask_mail import Message, Mail
from werkzeug.utils import secure_filename

mail = Mail(app)

@app.route('/')
def root():
    return redirect('/home')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/hotsauce')
def hotsauce_page():
    return render_template('hotsauce.html')

@app.route('/onlineorder')
def onlineorder_page():
    return render_template('OnlineOrdering.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply_page():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        resume = request.files.get('resume')
        criminal_history = request.form.get('criminal_history')
        explain_crime = request.form.get('explain_crime')
        # Compose email body
        body = f"""New application received:\n\nName: {name}\nEmail: {email}\nPhone: 
                {number} \n"""

        msg = Message(
            subject="New Taco Boy Job Application",
            recipients=[os.getenv("MAIL_USERNAME")],
            body=body
        )

        # Attach PDF if uploaded
        if resume and resume.filename.endswith('.pdf'):
            filename = secure_filename(resume.filename)
            msg.attach(filename, "application/pdf", resume.read())
            flash('Application submitted! Resume uploaded and emailed.')
        else:
            flash('Application submitted and emailed!')

        mail.send(msg)
        return redirect(url_for('apply_page'))

    return render_template('apply.html')

@app.route('/menu')
def menu_page():
    return render_template('menu.html')