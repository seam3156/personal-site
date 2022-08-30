#! venv/bin/python

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/home/")
@app.route("/")
def home():
    return render_template("home.html", title='home', num=100)

@app.route("/about/")
def about():
    return render_template("about.html", title='About')

app.run(host='0.0.0.0', port=5000, debug=True)