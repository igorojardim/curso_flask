from flask import render_template
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/")
@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print(form.username.data)

    return render_template("login.html", form=form)



@app.route("/teste/<info>")
@app.route("/teste", defaults = {"info": None})
def teste(info):
    r = User.query.filter_by(password="321123").all()

    print(r.name, r.email, r.username)

    return "ok"
    
    db.session.add(user)
    db.session.commit()

