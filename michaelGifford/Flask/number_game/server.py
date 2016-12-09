from flask import Flask, render_template, request, redirect, session
import random # import the random module
app = Flask(__name__)
# app.run(host= '0.0.0.0')
app.secret_key = 'NINJAZZZZZZZZZ!'


@app.route('/')
def index():
    # print (session['randomNum'])
    # session['randomNum'] = random.randint(1,100)
    # session['guess'] = 0
    # session['message'] = 'Hello'
    if 'guess' not in session:
        session['guess'] = 0
    if 'randomNum' not in session:
        session['randomNum'] = random.randint(1,100)
    if 'message' not in session:
        session['message'] = 'Hello'

    else:
        if int(session['guess']) < session['randomNum']:
            session['message'] = 'Too low!'
        elif int(session['guess']) > session['randomNum']:
            session['message'] = 'Too high!'
        elif int(session['guess']) == session['randomNum']:
            session['message'] = 'You got it right! {} was the number!'.format(session['randomNum'])
            session['randomNum'] = random.randint(1,100)
        else:
            session['message'] = 'Something went terribly wrong!'

    return render_template("index.html")


@app.route('/guess', methods=['post'])
def guess():
    session['guess'] = request.form['guess']
    return redirect('/')

app.run(debug=True) # run our server
