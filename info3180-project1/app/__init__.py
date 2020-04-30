from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://info3180-user:unlock@localhost/info3180-proj1" - local database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://liksbqgocctrmk:4d1659399cf74a6fc2e0ae82bce40fde99db170ce1e2af30824df56de3a63ef4@ec2-50-17-227-28.compute-1.amazonaws.com:5432/ddqjam3m7ipl4n'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
