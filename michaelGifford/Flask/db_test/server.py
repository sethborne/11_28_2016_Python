from flask import Flask, render_template, request, redirect, flash, session
from db import MySQLConnector
app = Flask(__name__)
app.secret_key = 'NINJAZ!'

mysql = MySQLConnector(app, 'world')

print (mysql.query_db("SELECT * FROM countries"))

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def form():
    session['name']=request.form['name']
    session['dojo']=request.form['dojo']
    session['language']=request.form['language']
    session['comment']=request.form['comment']

    valid = True
    if len(session['name']) < 1:
        flash("Name cannot be empty!")
        valid = False
    if len(session['comment']) < 1:
        flash("Comment cannot be empty!")
        valid = False
    if len(session['comment']) > 121:
        flash("Comment cannot more than 120 characters!")
        valid = False
    if len(session['dojo']) < 1:
        flash("Dojo cannot be empty!")
        valid = False
    if len(session['language']) < 1:
        flash("Language cannot be empty!")
        valid = False
    print (session)
    if valid:
        print (session)
        return render_template("result.html", form=session)
    return render_template("index.html")

app.run(debug=True) # run our server
