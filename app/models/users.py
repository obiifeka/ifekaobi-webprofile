from app import db 
from routes.api import  user

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.string(50))