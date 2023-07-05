from flask import  render_template,request
from flask  import  Blueprint
 

api  = Blueprint('api', __name__)

@api.route('/user/<name>')
def create_user(name):    
      return {'user': user.name}
  



 