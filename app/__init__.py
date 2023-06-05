from flask import Flask
#from flask_cors import CORS
#from flask_wtf.csrf import CSRFProtect
import secrets
from flask_sqlalchemy import SQLAlchemy
#from flask_security import SQLAlchemyUserDatastore
#from flask_security.core import UserMixin
#from flask_migrate import Migrate
from .secrets import  *

app=Flask(__name__)


app.config['SECRET_KEY'] = "ryrithgo7t8ookihgkj"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'.format(db_user=db_user, db_password=db_password,db_host=db_host,db_name=db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#migrate = Migrate(app, db)
print(db)
# csrf = CSRFProtect(app)
# CORS(app)



from .route import * 