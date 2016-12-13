from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")


@app.route('/result', methods=['POST'])
def form():
    data = {
    'name':request.form['name'],
    'dojo':request.form['dojo'],
    'language':request.form['language'],
    'comment':request.form['comment']
    }
    print (data)
    # redirects back to the '/' route
    # return redirect('/')
    return render_template("result.html", form=data)

app.run(debug=True) # run our server
