#! venv/bin/python

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/home/")
@app.route("/")
def home():
    return render_template("home.html", title='Home')

@app.route("/about/")
def about():
    return render_template("about.html", title='About')

@app.route("/projects/")
def projects():
    return render_template("projects.html", title = 'Projects')

if '__main__' == __name__:
    app.run(debug=True, host='0.0.0.0', port=5001)
