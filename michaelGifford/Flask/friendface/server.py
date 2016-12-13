from flask import Flask, request, redirect, render_template, session, flash
from flask_bcrypt import Bcrypt
from db import MySQLConnector
import re
import datetime

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = "loginregistration"
mysql = MySQLConnector(app,'friendface')

'''
NOTE: The code is a mess and redundant in places. I'd like to clean it up by moving duplicate code to functions and modularize it, but I think my time is best spend moving along the course to Django.

-Michael :-)
'''

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
    if not 'id' in session:
        data = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
            'confirm': ''
        }
        session['id'] = ''
        return render_template('login.html',data=data)
    elif session['id'] == '':
        data = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
            'confirm': ''
        }
        return render_template('login.html',data=data)
    else:
        data = {'id': session['id']}
        query = "SELECT first_name, last_name, email, created_at, modified_at FROM users WHERE id = :id"
        user = mysql.query_db(query, data)
        print(user)

        #GET ALL POSTS
        query = "SELECT posts.id, posts.content, posts.created_at, posts.modified_at, posts.deleted, users.first_name, users.last_name, users.id AS user_id, TIMEDIFF(NOW(),posts.created_at) AS age FROM posts JOIN users ON users.id = posts.user_id ORDER BY created_at DESC;"

        data['posts'] = mysql.query_db(query, data)
        # posts = ''
        comments = {}
        for post in data['posts']:
            # print (post['id'])

            # timeDiff = "declare @StartDate datetime, @EndDate datetime SELECT @StartDate = created_at,NOW()' SELECT convert(varchar(5),DateDiff(s, @startDate, @EndDate)/3600)+':'+convert(varchar(5),DateDiff(s, @startDate, @EndDate)%3600/60)+':'+convert(varchar(5),(DateDiff(s, @startDate, @EndDate)%60)) as [hh:mm:ss]"

            comments[post['id']] = mysql.query_db('SELECT comments.id, comments.comment, comments.created_at, comments.modified_at, comments.deleted, users.first_name, users.last_name, users.id AS user_id, TIMEDIFF(NOW(),comments.created_at) AS age FROM comments JOIN users ON users.id = comments.user_id WHERE post_id = :id',{'id':post['id']})
            # comments[post['id']]['age'] = datetime.datetime.now()-comments[post['id']]['created_at']
        print(comments)
        return render_template('index.html',user=user,posts=data['posts'],comments=comments)

@app.route('/profile/<userId>')
def userProfile(userId):
    data = {'id': userId}
    query = "SELECT posts.id, posts.content, posts.created_at, posts.modified_at, users.first_name, users.last_name, users.id AS user_id FROM posts JOIN users ON users.id = posts.user_id WHERE posts.user_id = :id ORDER BY created_at DESC;"

    # query = "SELECT id, content, created_at, modified_at FROM posts WHERE user_id = :id"
    user = mysql.query_db(query, data)
    data['posts'] = mysql.query_db(query, data)
    # data['posts']['ageCalc'] = str(data['post']['age'])
    # posts = ''
    comments = {}
    for post in data['posts']:
        # print (post['id'])
        comments[post['id']] = mysql.query_db('SELECT comments.id, comments.comment, comments.created_at, comments.modified_at, users.first_name, users.last_name, users.id AS user_id FROM comments JOIN users ON users.id = comments.user_id WHERE post_id = :id',{'id':post['id']})
    print(data['posts'])
    return render_template('index.html',user=user,posts=data['posts'],comments=comments)
    return render_template('index.html',user=user)


@app.route('/login', methods=['POST'])
def userLogin():
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    query = "SELECT id, password FROM users WHERE email = :email"
    user = mysql.query_db(query, data)
    if len(user) < 1:
        flash('EMail not found.')
        return redirect('/')
    elif bcrypt.check_password_hash(user[0]['password'],data['password']):
        session['id'] = user[0]['id']
        return redirect('/')
    else:
        flash("Incorrect email and password."+str(user[0]['id'])+data['password'])
    return redirect('/')

@app.route('/logout', methods=['POST'])
def userLogout():
    session['id'] = ''
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
    return valid


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
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, modified_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW());"
        data['user'] = mysql.query_db(query, data)
        data['blog'] = mysql.query_db('INSERT INTO blogs (name,created_at,modified_at) VALUES (:first_name,NOW(),NOW());', data)
        admin = mysql.query_db('INSERT INTO admins (blog_id,user_id,created_at,modified_at) VALUES (:blog,:user,NOW(),NOW());', data)
        session['id'] = data['user']
        print (session['id'])
        return redirect('/')
    else:
        return render_template('login.html',data=data)

@app.route('/user')
def showUser():
    session['id'] = data['id']
    query= "SELECT * FROM users"
    showUser = mysql.query_db(query, session['id'])
    return redirect('user.html')

@app.route('/process', methods=['POST'])
def processForm():
    data = {
        'id': session['id'],
        'form': request.form['form'],
        'content': request.form['content']
    }
    if data['form'] == 'search':
        pass
        # print (data['content'])
        # query= "SELECT * FROM posts WHERE content LIKE :content"
        # posts = mysql.query_db(query,data)
        return render_template('search.html',posts=posts)
    else:
        if data['form'] == 'post':
            query= "INSERT INTO posts (user_id,content,created_at,modified_at,blog_id) VALUES (:id, :content, NOW(), NOW(),:id);"
        elif data['form'] == 'comment':
            data['post_id'] = request.form['post_id']
            query= "INSERT INTO comments (comment,post_id,user_id,created_at,modified_at) VALUES (:content,:post_id,:id,NOW(),NOW());"
        action = mysql.query_db(query, data)
        print (action)
        return redirect('/')

@app.route('/delete/<itemType>/<itemId>', methods=['POST'])
def delete(itemType,itemId):
    data = {
        'id': session['id'],
        'item_id': itemId,
        'type': itemType,
        'value': str(1)
    }
    if itemType == 'posts':
        query = "UPDATE posts SET deleted = :value WHERE (id = :item_id AND user_id = :id);"
    elif itemType == 'comments':
        query = "UPDATE comments SET deleted = :value WHERE (id = :item_id AND user_id = :id);"
    print(data)
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/search', methods=['POST','GET'])
def search():
    data = {
        'id': session['id'],
        'form': request.form['form'],
        'content': request.form['content']
    }
    data = {'id': session['id']}
    query = "SELECT first_name, last_name, email, created_at, modified_at FROM users WHERE id = :id"
    user = mysql.query_db(query, data)
    SEARCH_REGEX = re.compile(r'data["content"]')
    #GET ALL POSTS
    query = "SELECT posts.id, posts.content, posts.created_at, posts.modified_at, users.first_name, users.last_name, users.id AS user_id FROM posts JOIN users ON users.id = posts.user_id WHERE posts.content LIKE '%:content%';"
    # data['posts'] = mysql.query_db(query, data)
    data['posts'] = 'Search ain\'t working!'
    posts = data['posts']
    comments = {}
    # for post in data['posts']:
        # print (post['id'])
        # comments[post['id']] = mysql.query_db('SELECT comments.id, comments.comment, comments.created_at, comments.modified_at, users.first_name, users.last_name, users.id AS user_id FROM comments JOIN users ON users.id = comments.user_id WHERE post_id = :id',{'id':post['id']})
    return render_template('search.html',user=user,posts=data['posts'],comments=comments)

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
    query = "SELECT * FROM posts WHERE id = :id"
    data = {'id': session['id']}
    post = mysql.query_db(query, data)
    print(post)

    return render_template('user.html', post=post)

# def deleteMessage():
#     query = "delete from posts where id = :id"
#     data = {'id' : id}
#     mysql.query_db(query, data)
#     return redirect('/user/<user_id>')


app.run(debug=True, host='0.0.0.0')
