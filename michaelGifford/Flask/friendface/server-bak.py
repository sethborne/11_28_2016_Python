from flask import Flask, request, redirect, render_template, session, flash
from db import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)

mysql = MySQLConnector(app,'friendface')
bcrypt = Bcrypt(app)

print('Initiating FriendFace ...')

@app.route('/')
def index():
    return render_template('index.html')

pwd = bcrypt.generate_password_hash('coding')
print (pwd)
print (bcrypt.check_password_hash(pwd, 'coding'))

app.run(debug=True)
