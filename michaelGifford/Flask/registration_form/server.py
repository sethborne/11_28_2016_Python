from flask import Flask, render_template, request, redirect, flash, session
import re
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'NINJAZZZ!'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
BDAY_REGEX = re.compile(r'\d\d\/\d\d\/\d\d\d\d')
bday = ''
PWD_REGEX = re.compile(r'')

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def form():
    session['first_name']=request.form['first_name']
    session['last_name']=request.form['last_name']
    session['birth_date']=request.form['birth_date']
    session['email']=request.form['email']
    session['password']=request.form['password']
    session['password2']=request.form['password2']


    valid = True
    if len(session['first_name']) < 1:
        flash("First Name cannot be empty!")
        valid = False
    if len(session['last_name']) < 1:
        flash("Last Name cannot be empty!")
        valid = False
    if len(session['email']) < 1:
        flash("Email cannot be empty!")
        valid = False
    elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Address")
        valid = False
    if len(session['password']) < 1:
        flash("Password cannot be empty!")
        valid = False
    elif session['password'] != session['password2']:
        flash("Password Confirmation did not pass!")
        valid = False
        if len(session['password']) < 9:
            flash("Password must at least 8 characters!")
            valid = False
        if str.isalpha(str(session['password'])):
            flash("Password must be alphanumeric!")
            valid = False
        elif str.isint(str(session['password'])):
            flash("Password must be alphanumeric!")
            valid = False
        if str.islower(session['password']) or str.isupper(session['password']):
            flash("Password must contain upper and lower case characters!")
        valid = False
    else:
        session['password_status'] = 'valid'
    if len(session['birth_date']) < 1:
        flash("Birth Date cannot be empty!")
        valid = False
    elif BDAY_REGEX.match(session['birth_date']):
        bday = datetime.strptime(session['birth_date'],'%m/%d/%Y')
        if bday > datetime.now():
            flash("Are you a time traveler? Birth date must be in past.")
            valid = False
    elif not BDAY_REGEX.match(session['birth_date']):
        flash("Birth Date not formatted correctly! {}".format(session['birth_date']))
        valid = False


    # print (bday)
    # print (datetime.now())
    print (session)

    if valid:
        print (session)
        return render_template("result.html")
    return render_template("index.html")

app.run(debug=True) # run our server
