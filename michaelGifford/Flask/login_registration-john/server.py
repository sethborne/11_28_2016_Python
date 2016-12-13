from flask import Flask, request, redirect, render_template, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
import re
import datetime

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = "loginregistration"

mysql = MySQLConnector(app,'friendface')

pwd_hash = ( bcrypt.generate_password_hash('Codingdojo1'))
print(bcrypt.check_password_hash(pwd_hash,'Codingdojo1'))
pwd_hash = ( bcrypt.generate_password_hash('Codingdojo1'))
print(bcrypt.check_password_hash(pwd_hash,'Codingdojo1'))
pwd_hash = ( bcrypt.generate_password_hash('Codingdojo1'))
print(bcrypt.check_password_hash(pwd_hash,'Codingdojo1'))


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SPACE_REGEX = re.compile(r'\S+')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9.+=_-]+$')
UPPER_CASE_REGEX = re.compile(r'[A-Z]')
NUMBER_REGEX = re.compile(r'[0-9]+')
ILLEGAL_REGEX = re.compile(r'[~`()+={}|\\:;\'\"<>,.?/]')

today = datetime.datetime.today().strftime("%Y-%m-%d")

@app.route('/')
def index():
    # users = mysql.query_db("select * from users")
    # print(users)
    # return render_template('index.html')
    if not id in session:
        session['id'] = ""
        return render_template('login.html')
    elif sesion['id'] == "":
        return render_template('login.html')
    else:
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def userLogin():
    data = {
        'email': request.form['email'],
        'pw_hash': bcrypt.generate_password_hash(request.form['password'])
    }
    query = "select id, password from users where email = :email "
    # query = "select id from users"
    user = mysql.query_db(query, data)
    print(query, user)
    print(data['pw_hash'])
    print(user[0]['id'], user[0]['password'])
    print(bcrypt.check_password_hash(data['pw_hash'], user[0]['password']))
    if bcrypt.check_password_hash(data['pw_hash'], user[0]['password']):
        session['id'] = user[0]['id']
        return redirect("/")
    else:
        flash("Incorrect email and password.")
    return redirect('/')

def validateUsers(data):
    valid = True
    if len(data['first_name']) < 1:
        flash("First name must not be empty!")
        valid = False
    elif not NAME_REGEX.match(data['first_name']):
        flash("First name must contain letters only!")
        valid = False
    if len(data['last_name']) < 1:
        flash("Last name must not be empty")
        valid = False
    elif not NAME_REGEX.match(data['last_name']):
        flash("Last name must contain letters only!")
        valid = False
    if len(data['email']) < 1:
        flash("Email must not be empty!")
        valid = False
    elif not EMAIL_REGEX.match(data['email']):
        flash("Email must be valid")
        valid = False
    if len(data['password']) < 8:
        flash("Password must be more than 8 characters!")
        valid = False
    elif not UPPER_CASE_REGEX.search(data['password']):
        flash("Must contain at least 1 uppercase letter.")
        valid = False
    elif not NUMBER_REGEX.search(data['password']):
        flash("Must contain at least 1 number.")
        valid = False
    elif ILLEGAL_REGEX.search(data['password']):
        flash("Password must not contain illegal characters (~`()+={}|\\:;\'\"<>,.?/)") #~`()+={}|\\:;\'\"<>,.?/
        valid = False
    # if data['confirmpassword'] != data['password']:
    #     flash("Password not confirmed.")
    #     valid = False
    if valid:
        flash("Congratulations! You are now registered!")
    return render_template('index.html')


# john = {'first_name': 'john',
# 'last_name': 'truong',
# 'email': 'Thientintruong@gmail.com',
# 'password': 'IamLegend2016'
#     }

@app.route('/signup', methods=['POST'])
def registerUser():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm': request.form['password2']
    }
    if validateUsers(data):
        data['pw_hash'] = bcrypt.generate_password_hash(data['password'])
        query = "insert into users (first_name, last_name, email, password, created_at, modified_at) values(:first_name, :last_name, :email, :pw_hash, NOW(), NOW() )"
        user = mysql.query_db(query, data)
        session['id'] = user
        return redirect('/')

@app.route('/user')
def showUser():
    session['id'] = data['id']
    query= "select * from users"
    showUser = mysql.query_db(query, session['id'])
    return redirect('user.html')


def inputMessage():
    if not SPACE_REGEX.match(request.form['content']):
        flash("Must have something")
    else:
        query = "insert into posts (id, content, created_at, modified_at) values (:id, :content, NOW(), NOW() )"

    data = {
        'content': request.form['content'],
        'id': 'id'
    }
    post = mysql.query_db(query,data)
    return redirect('/')

def showMessage():
    query = "select * from posts where id = :id "
    data = {'id' : session['id']}

    post = mysql.query_db(query, data)
    print(post)

    return render_template('user.html', post=post)

def deleteMessage():
    query = "delete from posts where id = :id"
    data = {'id' : id}
    mysql.query_db(query, data)
    return redirect('/user/<user_id>')


app.run(debug=True)
