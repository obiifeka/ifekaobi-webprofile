from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from .secrets import *
from  .routes.register import  main
from  .routes.services import  products
from  .routes.api import  api

app = Flask(__name__)


app.config['SECRET_KEY'] = "ryrithgo7t8ookihgkj"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'.format(db_user=db_user, db_password=db_password,db_host=db_host,db_name=db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index1.html')
    return render_template('index1.html')

app.register_blueprint(main)
app.register_blueprint(products)
app.register_blueprint(api)







