from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
UPLOAD_FOLDER = "./app/static/uploads"


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:nesha032898@localhost/people"
#app.config['SQLALCHEMY_DATABASE_URI']= "postgresql://oxfumqjlrqlycs:45a5b5a9fbd0f753ef38400a2ab8f27db48e5d996e4cbc7a72c29e2a0c8d3f5f@ec2-52-201-55-4.compute-1.amazonaws.com:5432/d9l9qglanjif6p"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['SECRET_KEY']= "MYKEY"
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER



app.config.from_object(__name__)
from app import views
