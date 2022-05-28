from enum import unique
import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


class Connection():
    def connection(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Ощлук171@localhost:8888/Users"
        db = SQLAlchemy(app)
        migrate = Migrate(app, db)
        return db