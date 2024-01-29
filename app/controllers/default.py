from flask import render_template
from app import app

@app.route("/", defaults={"user":None})
@app.route("/index/<user>")
def index(user):
    return render_template("index.html", user=user)
