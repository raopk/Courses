import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    number = random.randint(0,1)
    return render_template("index.html", number=number)

@app.route("/hello")
def hello():
    name = request.args.get("name")
    if not name: 
        return render_template("failure.html")
    return render_template("hello.html", name=name)
