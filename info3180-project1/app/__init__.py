from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
UPLOAD_FOLDER = "./app/static/uploads"


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:nesha032898@localhost/people"
#SQLALCHEMY_DATABASE_URI= 'postgresql://liksbqgocctrmk:4d1659399cf74a6fc2e0ae82bce40fde99db170ce1e2af30824df56de3a63ef4@ec2-50-17-227-28.compute-1.amazonaws.com:5432/ddqjam3m7ipl4n'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['SECRET_KEY']= "MYKEY"
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER



app.config.from_object(__name__)
from app import views
