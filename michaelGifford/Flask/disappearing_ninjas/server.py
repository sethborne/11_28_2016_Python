from flask import Flask, render_template, request, redirect, flash, session, url_for, send_from_directory
app = Flask(__name__)
app.secret_key = 'NINJAZZZZ!'


@app.route('/')
def index():
    image = 'tmnt.png'
    ninja = 'TNMT!'
    color = 'black'
    ninja = 'No Ninjas Here!'
    image = 'manhole.jpg'

    data = {}
    data['ninja'] = ninja
    data['color'] = color
    data['image'] = url_for('static',filename=image)

    print (data)

    return render_template("ninjas.html", data=data)


@app.route('/ninja/')
def tmnt():

    image = 'tmnt.png'
    ninja = 'TNMT!'
    color = 'green'

    data = {}
    data['ninja'] = ninja
    data['color'] = color
    data['image'] = url_for('static',filename=image)

    print (data)

    return render_template("ninjas.html", data=data)


@app.route('/ninja/<color>')
def ninja(color):
    print (color)

    if len(color) < 1:
        image = 'tmnt.png'
        ninja = 'TNMT!'
    elif color == 'red':
        image = 'raphael.jpg'
        ninja = 'Raphael'
    elif color == 'blue':
        image = 'leonardo.jpg'
        ninja = 'Leonardo'
    elif color == 'purple':
        image = 'donatello.jpg'
        ninja = 'Donatello'
    elif color == 'orange':
        image = 'michelangelo.jpg'
        ninja = 'Michelangelo'
    else:
        image = 'notapril.jpg'
        ninja = 'Error 404 Not April'
        color = ''

    data = {}
    data['ninja'] = ninja
    data['color'] = color
    data['image'] = url_for('static',filename=image)

    print (data)

    return render_template("ninjas.html", data=data)

@app.route('/ninjas/')
def ninjas():
    return redirect("/ninja")

@app.route('/static/images/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static', 'images'), filename)


app.run(debug=True) # run our server
