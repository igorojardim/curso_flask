from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
import psycopg2

app = Flask(__name__)

# Configurações do banco de dados PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:verdao80@localhost:5432/desenvolvimento'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__: "users"
    __table_args__ = {'schema': 'db_flask'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
    
    def __repr__(self):
        return "<User %r>" % self.username
    

class Post(db.Model):
    __tablename__: "posts"
    __table_args__ = {'schema': 'db_flask'}

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
    
    def __repr__(self):
        return "<Post %r>" % self.id
    
    
class Follow(db.Model):
    __tablename__ = "follows"
    __table_args__ = {'schema': 'db_flask'}

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, nullable=False)
    followed_id = db.Column(db.Integer, nullable=False)

    def __init__(self, follower_id, followed_id):
        self.follower_id = follower_id
        self.followed_id = followed_id
    
    def __repr__(self):
        return "<Follow %r>" % self.id
    
with app.app_context():
    db.drop_all()
    db.create_all()