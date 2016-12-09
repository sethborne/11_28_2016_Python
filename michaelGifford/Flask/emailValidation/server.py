from flask import Flask, render_template, request, redirect, flash, session

import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'My secret key'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'emails')
# an example of running a query

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    print request.form['email']
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Please enter a valid email')
        print 'invalid email'
        return redirect('/')
    else:
        session['email'] = request.form['email']
        query = "INSERT into emails (address, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {'email': request.form['email']}
        print 'valid'
        insert_at_id = mysql.query_db(query, data)
        print insert_at_id
        return redirect('/success')

@app.route('/success')
def success():
    emails =  mysql.query_db("SELECT * FROM emails")

    return render_template('success.html', emails=emails)




app.run(debug=True)
