from flask import  render_template,request
from flask  import  Blueprint


products  = Blueprint('products', __name__)


@products.route('/laptops',methods=['GET','POST'])
def laptops():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('laptops.html')
    return render_template('laptops.html')

@products.route('/props',methods=['GET','POST'])
def props():
    if request.method=='POST': 
        # Handle POST Request here
        return render_template('props.html')
    return render_template('props.html')

@products.route('/profile/dashboard',methods=['GET','POST'])
def prodile_dashboard():
    if request.method=='POST': 
        # Handle POST Request here
        return render_template('profile/dashboard.html')
    return render_template('profile/dashboard.html')

