from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

app.config['SECRET_KEY'] = "ryrithgo7t8ookihgkj"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'.format(db_user=db_user, db_password=db_password,db_host=db_host,db_name=db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



