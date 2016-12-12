from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# app.run(host= '0.0.0.0')
app.secret_key = 'NINJAZZZZZZZZZ!'


counter = 0

@app.route('/')
def index():
    global counter
    counter += 1
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template("index.html", counter=counter)


@app.route('/ninja')
def ninja():
    global counter
    counter += 1
    return redirect('/')

@app.route('/hacker')
def hacker():
    global counter
    counter = -1
    return redirect('/')

@app.route('/ninja2')
def ninja2():
    session['count'] += 1
    return redirect('/')

@app.route('/hacker2')
def hacker2():
    session['count'] = -1
    return redirect('/')


@app.route('/form', methods=['post'])
def form():
    if request.form['action'] == 'ninja':
        session['count'] += 10
    elif request.form['action'] == 'hacker':
        session['count'] += 100
    return redirect('/')

app.run(debug=True) # run our server
