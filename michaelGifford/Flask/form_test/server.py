from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'NinjaChop!' # you need to set a secret key for security purposes

# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
   print ("Got Post Info")
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   email = request.form['email']
   # redirects back to the '/' route
   # here we add two properties to session to store the name and email
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   return redirect('/show') # noticed that we changed where we redirect to so that we can go to the page that displays the name and email!
   return redirect('/show')

@app.route('/show')
def show_user():
  return render_template('user.html')


app.run(debug=True) # run our server
