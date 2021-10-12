from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =''
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique = True)
    height_ = db.Column(db.Float)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_