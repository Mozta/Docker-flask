from flask import Flask, jsonify, send_from_directory
# from werkzeug.utils import send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
import dotenv


dotenv.load_dotenv()


app = Flask(__name__)
app.config.from_object('project.config.Config')
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.route('/')
def home():
    return jsonify(message="Welcome to my Flask app with Docker!")


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename)
