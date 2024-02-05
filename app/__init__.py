from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import psycopg2


app = Flask(__name__)

# Configurações do banco de dados PostgreSQL
app.config.from_object('config')

db = SQLAlchemy(app)
#migrate = Migrate(app, db)

#manager = Manager(app)
#manager.add_command('db', MigrateCommand)
from app.models import tables
from app.controllers import default