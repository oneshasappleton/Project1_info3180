from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
UPLOAD_FOLDER = "./app/static/uploads"


#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://onesha2:nesha032898@localhost/people1"
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://uzxbkplvhudktl:27ef4efb8117a57d3a5e30d67b60a0372d61a20d1c8a3c14e24c4de1f8004976@ec2-18-233-32-61.compute-1.amazonaws.com:5432/d9hdia2a9rnrm1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['SECRET_KEY']= "MYKEY"
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER



app.config.from_object(__name__)
from app import views
